import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'
import { Observable, of, from } from '../rxjsStub';
import {mergeMap, map} from  '../rxjsStub';
import { AuthLoginPost200Response } from '../models/AuthLoginPost200Response';
import { AuthLoginPostRequest } from '../models/AuthLoginPostRequest';

import { DefaultApiRequestFactory, DefaultApiResponseProcessor} from "../apis/DefaultApi";
export class ObservableDefaultApi {
    private requestFactory: DefaultApiRequestFactory;
    private responseProcessor: DefaultApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: DefaultApiRequestFactory,
        responseProcessor?: DefaultApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new DefaultApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new DefaultApiResponseProcessor();
    }

    /**
     * Validates user credentials and returns an access token if successful.
     * Authenticate User
     * @param authLoginPostRequest 
     */
    public authLoginPostWithHttpInfo(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Observable<HttpInfo<AuthLoginPost200Response>> {
        const requestContextPromise = this.requestFactory.authLoginPost(authLoginPostRequest, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.authLoginPostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Validates user credentials and returns an access token if successful.
     * Authenticate User
     * @param authLoginPostRequest 
     */
    public authLoginPost(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Observable<AuthLoginPost200Response> {
        return this.authLoginPostWithHttpInfo(authLoginPostRequest, _options).pipe(map((apiResponse: HttpInfo<AuthLoginPost200Response>) => apiResponse.data));
    }

}
