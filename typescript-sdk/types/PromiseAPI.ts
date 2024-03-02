import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'

import { AuthLoginPost200Response } from '../models/AuthLoginPost200Response';
import { AuthLoginPostRequest } from '../models/AuthLoginPostRequest';
import { ObservableDefaultApi } from './ObservableAPI';

import { DefaultApiRequestFactory, DefaultApiResponseProcessor} from "../apis/DefaultApi";
export class PromiseDefaultApi {
    private api: ObservableDefaultApi

    public constructor(
        configuration: Configuration,
        requestFactory?: DefaultApiRequestFactory,
        responseProcessor?: DefaultApiResponseProcessor
    ) {
        this.api = new ObservableDefaultApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Deletes the user account.
     * Delete User
     */
    public authDeleteDeleteWithHttpInfo(_options?: Configuration): Promise<HttpInfo<void>> {
        const result = this.api.authDeleteDeleteWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * Deletes the user account.
     * Delete User
     */
    public authDeleteDelete(_options?: Configuration): Promise<void> {
        const result = this.api.authDeleteDelete(_options);
        return result.toPromise();
    }

    /**
     * Validates user credentials and returns an access token if successful.
     * Authenticate User
     * @param authLoginPostRequest 
     */
    public authLoginPostWithHttpInfo(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<HttpInfo<AuthLoginPost200Response>> {
        const result = this.api.authLoginPostWithHttpInfo(authLoginPostRequest, _options);
        return result.toPromise();
    }

    /**
     * Validates user credentials and returns an access token if successful.
     * Authenticate User
     * @param authLoginPostRequest 
     */
    public authLoginPost(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<AuthLoginPost200Response> {
        const result = this.api.authLoginPost(authLoginPostRequest, _options);
        return result.toPromise();
    }

    /**
     * Creates a new user account.
     * Register User
     * @param authLoginPostRequest 
     */
    public authRegisterPostWithHttpInfo(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<HttpInfo<void>> {
        const result = this.api.authRegisterPostWithHttpInfo(authLoginPostRequest, _options);
        return result.toPromise();
    }

    /**
     * Creates a new user account.
     * Register User
     * @param authLoginPostRequest 
     */
    public authRegisterPost(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<void> {
        const result = this.api.authRegisterPost(authLoginPostRequest, _options);
        return result.toPromise();
    }


}



