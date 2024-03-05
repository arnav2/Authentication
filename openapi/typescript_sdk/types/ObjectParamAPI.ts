import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'

import { AuthDeletePostRequest } from '../models/AuthDeletePostRequest';
import { AuthLoginPostRequest } from '../models/AuthLoginPostRequest';

import { ObservableAuthenticationApi } from "./ObservableAPI";
import { AuthenticationApiRequestFactory, AuthenticationApiResponseProcessor} from "../apis/AuthenticationApi";

export interface AuthenticationApiAuthDeletePostRequest {
    /**
     * 
     * @type AuthDeletePostRequest
     * @memberof AuthenticationApiauthDeletePost
     */
    authDeletePostRequest: AuthDeletePostRequest
}

export interface AuthenticationApiAuthLoginPostRequest {
    /**
     * 
     * @type AuthLoginPostRequest
     * @memberof AuthenticationApiauthLoginPost
     */
    authLoginPostRequest: AuthLoginPostRequest
}

export interface AuthenticationApiAuthLogoutPostRequest {
}

export interface AuthenticationApiAuthRegisterPostRequest {
    /**
     * 
     * @type AuthLoginPostRequest
     * @memberof AuthenticationApiauthRegisterPost
     */
    authLoginPostRequest: AuthLoginPostRequest
}

export class ObjectAuthenticationApi {
    private api: ObservableAuthenticationApi

    public constructor(configuration: Configuration, requestFactory?: AuthenticationApiRequestFactory, responseProcessor?: AuthenticationApiResponseProcessor) {
        this.api = new ObservableAuthenticationApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Delete user endpoint
     * @param param the request object
     */
    public authDeletePostWithHttpInfo(param: AuthenticationApiAuthDeletePostRequest, options?: Configuration): Promise<HttpInfo<void>> {
        return this.api.authDeletePostWithHttpInfo(param.authDeletePostRequest,  options).toPromise();
    }

    /**
     * Delete user endpoint
     * @param param the request object
     */
    public authDeletePost(param: AuthenticationApiAuthDeletePostRequest, options?: Configuration): Promise<void> {
        return this.api.authDeletePost(param.authDeletePostRequest,  options).toPromise();
    }

    /**
     * Login endpoint
     * @param param the request object
     */
    public authLoginPostWithHttpInfo(param: AuthenticationApiAuthLoginPostRequest, options?: Configuration): Promise<HttpInfo<void>> {
        return this.api.authLoginPostWithHttpInfo(param.authLoginPostRequest,  options).toPromise();
    }

    /**
     * Login endpoint
     * @param param the request object
     */
    public authLoginPost(param: AuthenticationApiAuthLoginPostRequest, options?: Configuration): Promise<void> {
        return this.api.authLoginPost(param.authLoginPostRequest,  options).toPromise();
    }

    /**
     * Logout endpoint
     * @param param the request object
     */
    public authLogoutPostWithHttpInfo(param: AuthenticationApiAuthLogoutPostRequest = {}, options?: Configuration): Promise<HttpInfo<void>> {
        return this.api.authLogoutPostWithHttpInfo( options).toPromise();
    }

    /**
     * Logout endpoint
     * @param param the request object
     */
    public authLogoutPost(param: AuthenticationApiAuthLogoutPostRequest = {}, options?: Configuration): Promise<void> {
        return this.api.authLogoutPost( options).toPromise();
    }

    /**
     * Register endpoint
     * @param param the request object
     */
    public authRegisterPostWithHttpInfo(param: AuthenticationApiAuthRegisterPostRequest, options?: Configuration): Promise<HttpInfo<void>> {
        return this.api.authRegisterPostWithHttpInfo(param.authLoginPostRequest,  options).toPromise();
    }

    /**
     * Register endpoint
     * @param param the request object
     */
    public authRegisterPost(param: AuthenticationApiAuthRegisterPostRequest, options?: Configuration): Promise<void> {
        return this.api.authRegisterPost(param.authLoginPostRequest,  options).toPromise();
    }

}
