// Code generated by protoc-gen-micro. DO NOT EDIT.
// source: animal_store_proto/restServiceGen.proto

package animal_store_proto

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/golang/protobuf/ptypes/empty"
	_ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	math "math"
)

import (
	context "context"
	api "go.unistack.org/micro/v3/api"
	client "go.unistack.org/micro/v3/client"
	server "go.unistack.org/micro/v3/server"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// Reference imports to suppress errors if they are not otherwise used.
var _ api.Endpoint
var _ context.Context
var _ client.Option
var _ server.Option

// Api Endpoints for AnimalStoreService service

func NewAnimalStoreServiceEndpoints() []*api.Endpoint {
	return []*api.Endpoint{
		&api.Endpoint{
			Name:    "AnimalStoreService.GetAnimal",
			Path:    []string{"/animal-store/v1/getAnimal"},
			Method:  []string{"GET"},
			Handler: "rpc",
		},
	}
}

// Client API for AnimalStoreService service

type AnimalStoreService interface {
	GetAnimal(ctx context.Context, in *AnimalReq, opts ...client.CallOption) (*AnimalRsp, error)
}

type animalStoreService struct {
	c    client.Client
	name string
}

func NewAnimalStoreService(name string, c client.Client) AnimalStoreService {
	return &animalStoreService{
		c:    c,
		name: name,
	}
}

func (c *animalStoreService) GetAnimal(ctx context.Context, in *AnimalReq, opts ...client.CallOption) (*AnimalRsp, error) {
	req := c.c.NewRequest(c.name, "AnimalStoreService.GetAnimal", in)
	out := new(AnimalRsp)
	err := c.c.Call(ctx, req, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// Server API for AnimalStoreService service

type AnimalStoreServiceHandler interface {
	GetAnimal(context.Context, *AnimalReq, *AnimalRsp) error
}

func RegisterAnimalStoreServiceHandler(s server.Server, hdlr AnimalStoreServiceHandler, opts ...server.HandlerOption) error {
	type animalStoreService interface {
		GetAnimal(ctx context.Context, in *AnimalReq, out *AnimalRsp) error
	}
	type AnimalStoreService struct {
		animalStoreService
	}
	h := &animalStoreServiceHandler{hdlr}
	opts = append(opts, api.WithEndpoint(&api.Endpoint{
		Name:    "AnimalStoreService.GetAnimal",
		Path:    []string{"/animal-store/v1/getAnimal"},
		Method:  []string{"GET"},
		Handler: "rpc",
	}))
	return s.Handle(s.NewHandler(&AnimalStoreService{h}, opts...))
}

type animalStoreServiceHandler struct {
	AnimalStoreServiceHandler
}

func (h *animalStoreServiceHandler) GetAnimal(ctx context.Context, in *AnimalReq, out *AnimalRsp) error {
	return h.AnimalStoreServiceHandler.GetAnimal(ctx, in, out)
}
