import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'

import { AuthLoginPost200Response } from '../models/AuthLoginPost200Response';
import { AuthLoginPostRequest } from '../models/AuthLoginPostRequest';

import { ObservableDefaultApi } from "./ObservableAPI";
import { DefaultApiRequestFactory, DefaultApiResponseProcessor} from "../apis/DefaultApi";

export interface DefaultApiAuthDeleteDeleteRequest {
}

export interface DefaultApiAuthLoginPostRequest {
    /**
     * 
     * @type AuthLoginPostRequest
     * @memberof DefaultApiauthLoginPost
     */
    authLoginPostRequest: AuthLoginPostRequest
}

export interface DefaultApiAuthRegisterPostRequest {
    /**
     * 
     * @type AuthLoginPostRequest
     * @memberof DefaultApiauthRegisterPost
     */
    authLoginPostRequest: AuthLoginPostRequest
}

export class ObjectDefaultApi {
    private api: ObservableDefaultApi

    public constructor(configuration: Configuration, requestFactory?: DefaultApiRequestFactory, responseProcessor?: DefaultApiResponseProcessor) {
        this.api = new ObservableDefaultApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Deletes the user account.
     * Delete User
     * @param param the request object
     */
    public authDeleteDeleteWithHttpInfo(param: DefaultApiAuthDeleteDeleteRequest = {}, options?: Configuration): Promise<HttpInfo<void>> {
        return this.api.authDeleteDeleteWithHttpInfo( options).toPromise();
    }

    /**
     * Deletes the user account.
     * Delete User
     * @param param the request object
     */
    public authDeleteDelete(param: DefaultApiAuthDeleteDeleteRequest = {}, options?: Configuration): Promise<void> {
        return this.api.authDeleteDelete( options).toPromise();
    }

    /**
     * Validates user credentials and returns an access token if successful.
     * Authenticate User
     * @param param the request object
     */
    public authLoginPostWithHttpInfo(param: DefaultApiAuthLoginPostRequest, options?: Configuration): Promise<HttpInfo<AuthLoginPost200Response>> {
        return this.api.authLoginPostWithHttpInfo(param.authLoginPostRequest,  options).toPromise();
    }

    /**
     * Validates user credentials and returns an access token if successful.
     * Authenticate User
     * @param param the request object
     */
    public authLoginPost(param: DefaultApiAuthLoginPostRequest, options?: Configuration): Promise<AuthLoginPost200Response> {
        return this.api.authLoginPost(param.authLoginPostRequest,  options).toPromise();
    }

    /**
     * Creates a new user account.
     * Register User
     * @param param the request object
     */
    public authRegisterPostWithHttpInfo(param: DefaultApiAuthRegisterPostRequest, options?: Configuration): Promise<HttpInfo<void>> {
        return this.api.authRegisterPostWithHttpInfo(param.authLoginPostRequest,  options).toPromise();
    }

    /**
     * Creates a new user account.
     * Register User
     * @param param the request object
     */
    public authRegisterPost(param: DefaultApiAuthRegisterPostRequest, options?: Configuration): Promise<void> {
        return this.api.authRegisterPost(param.authLoginPostRequest,  options).toPromise();
    }

}
