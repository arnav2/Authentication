import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'
import { Observable, of, from } from '../rxjsStub';
import {mergeMap, map} from  '../rxjsStub';
import { AuthDeletePostRequest } from '../models/AuthDeletePostRequest';
import { AuthLoginPostRequest } from '../models/AuthLoginPostRequest';

import { AuthenticationApiRequestFactory, AuthenticationApiResponseProcessor} from "../apis/AuthenticationApi";
export class ObservableAuthenticationApi {
    private requestFactory: AuthenticationApiRequestFactory;
    private responseProcessor: AuthenticationApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: AuthenticationApiRequestFactory,
        responseProcessor?: AuthenticationApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new AuthenticationApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new AuthenticationApiResponseProcessor();
    }

    /**
     * Delete user endpoint
     * @param authDeletePostRequest 
     */
    public authDeletePostWithHttpInfo(authDeletePostRequest: AuthDeletePostRequest, _options?: Configuration): Observable<HttpInfo<void>> {
        const requestContextPromise = this.requestFactory.authDeletePost(authDeletePostRequest, _options);

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
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.authDeletePostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Delete user endpoint
     * @param authDeletePostRequest 
     */
    public authDeletePost(authDeletePostRequest: AuthDeletePostRequest, _options?: Configuration): Observable<void> {
        return this.authDeletePostWithHttpInfo(authDeletePostRequest, _options).pipe(map((apiResponse: HttpInfo<void>) => apiResponse.data));
    }

    /**
     * Login endpoint
     * @param authLoginPostRequest 
     */
    public authLoginPostWithHttpInfo(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Observable<HttpInfo<void>> {
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
     * Login endpoint
     * @param authLoginPostRequest 
     */
    public authLoginPost(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Observable<void> {
        return this.authLoginPostWithHttpInfo(authLoginPostRequest, _options).pipe(map((apiResponse: HttpInfo<void>) => apiResponse.data));
    }

    /**
     * Logout endpoint
     */
    public authLogoutPostWithHttpInfo(_options?: Configuration): Observable<HttpInfo<void>> {
        const requestContextPromise = this.requestFactory.authLogoutPost(_options);

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
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.authLogoutPostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Logout endpoint
     */
    public authLogoutPost(_options?: Configuration): Observable<void> {
        return this.authLogoutPostWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<void>) => apiResponse.data));
    }

    /**
     * Register endpoint
     * @param authLoginPostRequest 
     */
    public authRegisterPostWithHttpInfo(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Observable<HttpInfo<void>> {
        const requestContextPromise = this.requestFactory.authRegisterPost(authLoginPostRequest, _options);

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
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.authRegisterPostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Register endpoint
     * @param authLoginPostRequest 
     */
    public authRegisterPost(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Observable<void> {
        return this.authRegisterPostWithHttpInfo(authLoginPostRequest, _options).pipe(map((apiResponse: HttpInfo<void>) => apiResponse.data));
    }

}
