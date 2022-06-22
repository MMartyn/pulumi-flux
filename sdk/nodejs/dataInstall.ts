// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function dataInstall(args: DataInstallArgs, opts?: pulumi.InvokeOptions): Promise<DataInstallResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("flux:index/dataInstall:DataInstall", {
        "baseurl": args.baseurl,
        "clusterDomain": args.clusterDomain,
        "components": args.components,
        "componentsExtras": args.componentsExtras,
        "imagePullSecrets": args.imagePullSecrets,
        "logLevel": args.logLevel,
        "namespace": args.namespace,
        "networkPolicy": args.networkPolicy,
        "registry": args.registry,
        "targetPath": args.targetPath,
        "tolerationKeys": args.tolerationKeys,
        "version": args.version,
        "watchAllNamespaces": args.watchAllNamespaces,
    }, opts);
}

/**
 * A collection of arguments for invoking DataInstall.
 */
export interface DataInstallArgs {
    baseurl?: string;
    clusterDomain?: string;
    components?: string[];
    componentsExtras?: string[];
    imagePullSecrets?: string;
    logLevel?: string;
    namespace?: string;
    networkPolicy?: boolean;
    registry?: string;
    targetPath: string;
    tolerationKeys?: string[];
    version?: string;
    watchAllNamespaces?: boolean;
}

/**
 * A collection of values returned by DataInstall.
 */
export interface DataInstallResult {
    readonly baseurl?: string;
    readonly clusterDomain?: string;
    readonly components?: string[];
    readonly componentsExtras?: string[];
    readonly content: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly imagePullSecrets?: string;
    readonly logLevel?: string;
    readonly namespace?: string;
    readonly networkPolicy?: boolean;
    readonly path: string;
    readonly registry?: string;
    readonly targetPath: string;
    readonly tolerationKeys?: string[];
    readonly version?: string;
    readonly watchAllNamespaces?: boolean;
}

export function dataInstallOutput(args: DataInstallOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<DataInstallResult> {
    return pulumi.output(args).apply(a => dataInstall(a, opts))
}

/**
 * A collection of arguments for invoking DataInstall.
 */
export interface DataInstallOutputArgs {
    baseurl?: pulumi.Input<string>;
    clusterDomain?: pulumi.Input<string>;
    components?: pulumi.Input<pulumi.Input<string>[]>;
    componentsExtras?: pulumi.Input<pulumi.Input<string>[]>;
    imagePullSecrets?: pulumi.Input<string>;
    logLevel?: pulumi.Input<string>;
    namespace?: pulumi.Input<string>;
    networkPolicy?: pulumi.Input<boolean>;
    registry?: pulumi.Input<string>;
    targetPath: pulumi.Input<string>;
    tolerationKeys?: pulumi.Input<pulumi.Input<string>[]>;
    version?: pulumi.Input<string>;
    watchAllNamespaces?: pulumi.Input<boolean>;
}
