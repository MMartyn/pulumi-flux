// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package flux

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func DataSync(ctx *pulumi.Context, args *DataSyncArgs, opts ...pulumi.InvokeOption) (*DataSyncResult, error) {
	var rv DataSyncResult
	err := ctx.Invoke("flux:index/dataSync:DataSync", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking DataSync.
type DataSyncArgs struct {
	Branch            *string  `pulumi:"branch"`
	Commit            *string  `pulumi:"commit"`
	GitImplementation *string  `pulumi:"gitImplementation"`
	Interval          *int     `pulumi:"interval"`
	Name              *string  `pulumi:"name"`
	Namespace         *string  `pulumi:"namespace"`
	PatchNames        []string `pulumi:"patchNames"`
	Secret            *string  `pulumi:"secret"`
	Semver            *string  `pulumi:"semver"`
	Tag               *string  `pulumi:"tag"`
	TargetPath        string   `pulumi:"targetPath"`
	Url               string   `pulumi:"url"`
}

// A collection of values returned by DataSync.
type DataSyncResult struct {
	Branch            *string `pulumi:"branch"`
	Commit            *string `pulumi:"commit"`
	Content           string  `pulumi:"content"`
	GitImplementation *string `pulumi:"gitImplementation"`
	// The provider-assigned unique ID for this managed resource.
	Id               string            `pulumi:"id"`
	Interval         *int              `pulumi:"interval"`
	KustomizeContent string            `pulumi:"kustomizeContent"`
	KustomizePath    string            `pulumi:"kustomizePath"`
	Name             *string           `pulumi:"name"`
	Namespace        *string           `pulumi:"namespace"`
	PatchFilePaths   map[string]string `pulumi:"patchFilePaths"`
	PatchNames       []string          `pulumi:"patchNames"`
	Path             string            `pulumi:"path"`
	Secret           *string           `pulumi:"secret"`
	Semver           *string           `pulumi:"semver"`
	Tag              *string           `pulumi:"tag"`
	TargetPath       string            `pulumi:"targetPath"`
	Url              string            `pulumi:"url"`
}

func DataSyncOutput(ctx *pulumi.Context, args DataSyncOutputArgs, opts ...pulumi.InvokeOption) DataSyncResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (DataSyncResult, error) {
			args := v.(DataSyncArgs)
			r, err := DataSync(ctx, &args, opts...)
			var s DataSyncResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(DataSyncResultOutput)
}

// A collection of arguments for invoking DataSync.
type DataSyncOutputArgs struct {
	Branch            pulumi.StringPtrInput   `pulumi:"branch"`
	Commit            pulumi.StringPtrInput   `pulumi:"commit"`
	GitImplementation pulumi.StringPtrInput   `pulumi:"gitImplementation"`
	Interval          pulumi.IntPtrInput      `pulumi:"interval"`
	Name              pulumi.StringPtrInput   `pulumi:"name"`
	Namespace         pulumi.StringPtrInput   `pulumi:"namespace"`
	PatchNames        pulumi.StringArrayInput `pulumi:"patchNames"`
	Secret            pulumi.StringPtrInput   `pulumi:"secret"`
	Semver            pulumi.StringPtrInput   `pulumi:"semver"`
	Tag               pulumi.StringPtrInput   `pulumi:"tag"`
	TargetPath        pulumi.StringInput      `pulumi:"targetPath"`
	Url               pulumi.StringInput      `pulumi:"url"`
}

func (DataSyncOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataSyncArgs)(nil)).Elem()
}

// A collection of values returned by DataSync.
type DataSyncResultOutput struct{ *pulumi.OutputState }

func (DataSyncResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataSyncResult)(nil)).Elem()
}

func (o DataSyncResultOutput) ToDataSyncResultOutput() DataSyncResultOutput {
	return o
}

func (o DataSyncResultOutput) ToDataSyncResultOutputWithContext(ctx context.Context) DataSyncResultOutput {
	return o
}

func (o DataSyncResultOutput) Branch() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.Branch }).(pulumi.StringPtrOutput)
}

func (o DataSyncResultOutput) Commit() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.Commit }).(pulumi.StringPtrOutput)
}

func (o DataSyncResultOutput) Content() pulumi.StringOutput {
	return o.ApplyT(func(v DataSyncResult) string { return v.Content }).(pulumi.StringOutput)
}

func (o DataSyncResultOutput) GitImplementation() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.GitImplementation }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o DataSyncResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v DataSyncResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o DataSyncResultOutput) Interval() pulumi.IntPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *int { return v.Interval }).(pulumi.IntPtrOutput)
}

func (o DataSyncResultOutput) KustomizeContent() pulumi.StringOutput {
	return o.ApplyT(func(v DataSyncResult) string { return v.KustomizeContent }).(pulumi.StringOutput)
}

func (o DataSyncResultOutput) KustomizePath() pulumi.StringOutput {
	return o.ApplyT(func(v DataSyncResult) string { return v.KustomizePath }).(pulumi.StringOutput)
}

func (o DataSyncResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o DataSyncResultOutput) Namespace() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.Namespace }).(pulumi.StringPtrOutput)
}

func (o DataSyncResultOutput) PatchFilePaths() pulumi.StringMapOutput {
	return o.ApplyT(func(v DataSyncResult) map[string]string { return v.PatchFilePaths }).(pulumi.StringMapOutput)
}

func (o DataSyncResultOutput) PatchNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v DataSyncResult) []string { return v.PatchNames }).(pulumi.StringArrayOutput)
}

func (o DataSyncResultOutput) Path() pulumi.StringOutput {
	return o.ApplyT(func(v DataSyncResult) string { return v.Path }).(pulumi.StringOutput)
}

func (o DataSyncResultOutput) Secret() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.Secret }).(pulumi.StringPtrOutput)
}

func (o DataSyncResultOutput) Semver() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.Semver }).(pulumi.StringPtrOutput)
}

func (o DataSyncResultOutput) Tag() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataSyncResult) *string { return v.Tag }).(pulumi.StringPtrOutput)
}

func (o DataSyncResultOutput) TargetPath() pulumi.StringOutput {
	return o.ApplyT(func(v DataSyncResult) string { return v.TargetPath }).(pulumi.StringOutput)
}

func (o DataSyncResultOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v DataSyncResult) string { return v.Url }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(DataSyncResultOutput{})
}
