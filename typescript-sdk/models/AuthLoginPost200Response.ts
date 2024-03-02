/**
 * Authentication System API
 * API for user authentication and management
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { HttpFile } from '../http/http';

export class AuthLoginPost200Response {
    /**
    * JWT access token
    */
    'accessToken'?: string;

    static readonly discriminator: string | undefined = undefined;

    static readonly attributeTypeMap: Array<{name: string, baseName: string, type: string, format: string}> = [
        {
            "name": "accessToken",
            "baseName": "accessToken",
            "type": "string",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return AuthLoginPost200Response.attributeTypeMap;
    }

    public constructor() {
    }
}

