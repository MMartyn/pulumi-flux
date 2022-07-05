# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'DataInstallResult',
    'AwaitableDataInstallResult',
    'data_install',
    'data_install_output',
]

@pulumi.output_type
class DataInstallResult:
    """
    A collection of values returned by DataInstall.
    """
    def __init__(__self__, baseurl=None, cluster_domain=None, components=None, components_extras=None, content=None, id=None, image_pull_secrets=None, log_level=None, namespace=None, network_policy=None, path=None, registry=None, target_path=None, toleration_keys=None, version=None, watch_all_namespaces=None):
        if baseurl and not isinstance(baseurl, str):
            raise TypeError("Expected argument 'baseurl' to be a str")
        pulumi.set(__self__, "baseurl", baseurl)
        if cluster_domain and not isinstance(cluster_domain, str):
            raise TypeError("Expected argument 'cluster_domain' to be a str")
        pulumi.set(__self__, "cluster_domain", cluster_domain)
        if components and not isinstance(components, list):
            raise TypeError("Expected argument 'components' to be a list")
        pulumi.set(__self__, "components", components)
        if components_extras and not isinstance(components_extras, list):
            raise TypeError("Expected argument 'components_extras' to be a list")
        pulumi.set(__self__, "components_extras", components_extras)
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_pull_secrets and not isinstance(image_pull_secrets, str):
            raise TypeError("Expected argument 'image_pull_secrets' to be a str")
        pulumi.set(__self__, "image_pull_secrets", image_pull_secrets)
        if log_level and not isinstance(log_level, str):
            raise TypeError("Expected argument 'log_level' to be a str")
        pulumi.set(__self__, "log_level", log_level)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if network_policy and not isinstance(network_policy, bool):
            raise TypeError("Expected argument 'network_policy' to be a bool")
        pulumi.set(__self__, "network_policy", network_policy)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if registry and not isinstance(registry, str):
            raise TypeError("Expected argument 'registry' to be a str")
        pulumi.set(__self__, "registry", registry)
        if target_path and not isinstance(target_path, str):
            raise TypeError("Expected argument 'target_path' to be a str")
        pulumi.set(__self__, "target_path", target_path)
        if toleration_keys and not isinstance(toleration_keys, list):
            raise TypeError("Expected argument 'toleration_keys' to be a list")
        pulumi.set(__self__, "toleration_keys", toleration_keys)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if watch_all_namespaces and not isinstance(watch_all_namespaces, bool):
            raise TypeError("Expected argument 'watch_all_namespaces' to be a bool")
        pulumi.set(__self__, "watch_all_namespaces", watch_all_namespaces)

    @property
    @pulumi.getter
    def baseurl(self) -> Optional[str]:
        return pulumi.get(self, "baseurl")

    @property
    @pulumi.getter(name="clusterDomain")
    def cluster_domain(self) -> Optional[str]:
        return pulumi.get(self, "cluster_domain")

    @property
    @pulumi.getter
    def components(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "components")

    @property
    @pulumi.getter(name="componentsExtras")
    def components_extras(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "components_extras")

    @property
    @pulumi.getter
    def content(self) -> str:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imagePullSecrets")
    def image_pull_secrets(self) -> Optional[str]:
        return pulumi.get(self, "image_pull_secrets")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[str]:
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="networkPolicy")
    def network_policy(self) -> Optional[bool]:
        return pulumi.get(self, "network_policy")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def registry(self) -> Optional[str]:
        return pulumi.get(self, "registry")

    @property
    @pulumi.getter(name="targetPath")
    def target_path(self) -> str:
        return pulumi.get(self, "target_path")

    @property
    @pulumi.getter(name="tolerationKeys")
    def toleration_keys(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "toleration_keys")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="watchAllNamespaces")
    def watch_all_namespaces(self) -> Optional[bool]:
        return pulumi.get(self, "watch_all_namespaces")


class AwaitableDataInstallResult(DataInstallResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return DataInstallResult(
            baseurl=self.baseurl,
            cluster_domain=self.cluster_domain,
            components=self.components,
            components_extras=self.components_extras,
            content=self.content,
            id=self.id,
            image_pull_secrets=self.image_pull_secrets,
            log_level=self.log_level,
            namespace=self.namespace,
            network_policy=self.network_policy,
            path=self.path,
            registry=self.registry,
            target_path=self.target_path,
            toleration_keys=self.toleration_keys,
            version=self.version,
            watch_all_namespaces=self.watch_all_namespaces)


def data_install(baseurl: Optional[str] = None,
                 cluster_domain: Optional[str] = None,
                 components: Optional[Sequence[str]] = None,
                 components_extras: Optional[Sequence[str]] = None,
                 image_pull_secrets: Optional[str] = None,
                 log_level: Optional[str] = None,
                 namespace: Optional[str] = None,
                 network_policy: Optional[bool] = None,
                 registry: Optional[str] = None,
                 target_path: Optional[str] = None,
                 toleration_keys: Optional[Sequence[str]] = None,
                 version: Optional[str] = None,
                 watch_all_namespaces: Optional[bool] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableDataInstallResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['baseurl'] = baseurl
    __args__['clusterDomain'] = cluster_domain
    __args__['components'] = components
    __args__['componentsExtras'] = components_extras
    __args__['imagePullSecrets'] = image_pull_secrets
    __args__['logLevel'] = log_level
    __args__['namespace'] = namespace
    __args__['networkPolicy'] = network_policy
    __args__['registry'] = registry
    __args__['targetPath'] = target_path
    __args__['tolerationKeys'] = toleration_keys
    __args__['version'] = version
    __args__['watchAllNamespaces'] = watch_all_namespaces
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('flux:index/dataInstall:DataInstall', __args__, opts=opts, typ=DataInstallResult).value

    return AwaitableDataInstallResult(
        baseurl=__ret__.baseurl,
        cluster_domain=__ret__.cluster_domain,
        components=__ret__.components,
        components_extras=__ret__.components_extras,
        content=__ret__.content,
        id=__ret__.id,
        image_pull_secrets=__ret__.image_pull_secrets,
        log_level=__ret__.log_level,
        namespace=__ret__.namespace,
        network_policy=__ret__.network_policy,
        path=__ret__.path,
        registry=__ret__.registry,
        target_path=__ret__.target_path,
        toleration_keys=__ret__.toleration_keys,
        version=__ret__.version,
        watch_all_namespaces=__ret__.watch_all_namespaces)


@_utilities.lift_output_func(data_install)
def data_install_output(baseurl: Optional[pulumi.Input[Optional[str]]] = None,
                        cluster_domain: Optional[pulumi.Input[Optional[str]]] = None,
                        components: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        components_extras: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        image_pull_secrets: Optional[pulumi.Input[Optional[str]]] = None,
                        log_level: Optional[pulumi.Input[Optional[str]]] = None,
                        namespace: Optional[pulumi.Input[Optional[str]]] = None,
                        network_policy: Optional[pulumi.Input[Optional[bool]]] = None,
                        registry: Optional[pulumi.Input[Optional[str]]] = None,
                        target_path: Optional[pulumi.Input[str]] = None,
                        toleration_keys: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        version: Optional[pulumi.Input[Optional[str]]] = None,
                        watch_all_namespaces: Optional[pulumi.Input[Optional[bool]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[DataInstallResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
