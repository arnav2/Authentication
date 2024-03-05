import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'

import { AuthDeletePostRequest } from '../models/AuthDeletePostRequest';
import { AuthLoginPostRequest } from '../models/AuthLoginPostRequest';
import { ObservableAuthenticationApi } from './ObservableAPI';

import { AuthenticationApiRequestFactory, AuthenticationApiResponseProcessor} from "../apis/AuthenticationApi";
export class PromiseAuthenticationApi {
    private api: ObservableAuthenticationApi

    public constructor(
        configuration: Configuration,
        requestFactory?: AuthenticationApiRequestFactory,
        responseProcessor?: AuthenticationApiResponseProcessor
    ) {
        this.api = new ObservableAuthenticationApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Delete user endpoint
     * @param authDeletePostRequest 
     */
    public authDeletePostWithHttpInfo(authDeletePostRequest: AuthDeletePostRequest, _options?: Configuration): Promise<HttpInfo<void>> {
        const result = this.api.authDeletePostWithHttpInfo(authDeletePostRequest, _options);
        return result.toPromise();
    }

    /**
     * Delete user endpoint
     * @param authDeletePostRequest 
     */
    public authDeletePost(authDeletePostRequest: AuthDeletePostRequest, _options?: Configuration): Promise<void> {
        const result = this.api.authDeletePost(authDeletePostRequest, _options);
        return result.toPromise();
    }

    /**
     * Login endpoint
     * @param authLoginPostRequest 
     */
    public authLoginPostWithHttpInfo(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<HttpInfo<void>> {
        const result = this.api.authLoginPostWithHttpInfo(authLoginPostRequest, _options);
        return result.toPromise();
    }

    /**
     * Login endpoint
     * @param authLoginPostRequest 
     */
    public authLoginPost(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<void> {
        const result = this.api.authLoginPost(authLoginPostRequest, _options);
        return result.toPromise();
    }

    /**
     * Logout endpoint
     */
    public authLogoutPostWithHttpInfo(_options?: Configuration): Promise<HttpInfo<void>> {
        const result = this.api.authLogoutPostWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * Logout endpoint
     */
    public authLogoutPost(_options?: Configuration): Promise<void> {
        const result = this.api.authLogoutPost(_options);
        return result.toPromise();
    }

    /**
     * Register endpoint
     * @param authLoginPostRequest 
     */
    public authRegisterPostWithHttpInfo(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<HttpInfo<void>> {
        const result = this.api.authRegisterPostWithHttpInfo(authLoginPostRequest, _options);
        return result.toPromise();
    }

    /**
     * Register endpoint
     * @param authLoginPostRequest 
     */
    public authRegisterPost(authLoginPostRequest: AuthLoginPostRequest, _options?: Configuration): Promise<void> {
        const result = this.api.authRegisterPost(authLoginPostRequest, _options);
        return result.toPromise();
    }


}



