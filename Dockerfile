FROM golang:1.17.12-buster

RUN mkdir /build
WORKDIR /build

COPY --from=swaggerapi/swagger-ui /usr/share/nginx/html/ /swagger-ui/

RUN apt-get update && apt-get -y install --no-install-recommends protobuf-compiler-grpc python3-grpc-tools libprotobuf-dev protobuf-compiler python3-pip python3-dev python3-setuptools  && rm -rf /var/lib/apt/lists/*

RUN go mod init proto && \
    go install github.com/envoyproxy/protoc-gen-validate@v0.3.0-java && \
    go install google.golang.org/protobuf/cmd/protoc-gen-go@latest && \
    go install github.com/srikrsna/protoc-gen-gotag@v0.5.0 && \
    go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger@v1.14.3 && \
    go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway@v1.14.3 && \
    go get google.golang.org/grpc@v1.28.0 && \
    go get github.com/google/googleapis@v0.0.0-20200324113624-36c0febd0fa7 && \
    go get github.com/grpc-ecosystem/grpc-gateway@v1.14.3 && \
    go get github.com/presnalex/protoc-gen-micro@v0.0.2 && \
    go get github.com/go-bindata/go-bindata/...

CMD rm -rf python && mkdir python && rm -rf go && mkdir go && \
        rm -rf grpc-gateway && mkdir grpc-gateway  && \
        rm -rf swagger && mkdir swagger  && \
        python3 -m grpc_tools.protoc \
          --validate_out=lang=go:go \
          --micro_out=go \
          --go_out=go \
          --python_out=python \
          --swagger_out=swagger \
          --grpc-gateway_out=grpc-gateway \
          --grpc_python_out=python \
          --swagger_opt=json_names_for_fields=true \
          -I=. \
          -I=/usr/include \
          -I=/go/pkg/mod/github.com/envoyproxy/protoc-gen-validate@v0.3.0-java \
          -I=/go/pkg/mod/github.com/srikrsna/protoc-gen-gotag@v0.5.0 \
          -I=/go/pkg/mod/github.com/google/googleapis@v0.0.0-20200324113624-36c0febd0fa7 \
          -I=/go/pkg/mod/github.com/grpc-ecosystem/grpc-gateway@v1.14.3 \
          */*.proto && \
        cd go && \
        protoc \
        -I=../ \
        -I=/usr/include \
        -I=/go/pkg/mod/github.com/envoyproxy/protoc-gen-validate@v0.3.0-java \
        -I=/go/pkg/mod/github.com/srikrsna/protoc-gen-gotag@v0.5.0 \
        -I=/go/pkg/mod/github.com/google/googleapis@v0.0.0-20200324113624-36c0febd0fa7 \
        -I=/go/pkg/mod/github.com/grpc-ecosystem/grpc-gateway@v1.14.3 \
        --gotag_out=xxx="xml+\"-\"":. \
        ../*/*.proto  && \
        cd .. && \
        if [ $(grep -RHl protoc-gen-swagger *_proto | wc -l) -eq 1 ]; then \
        FILE=$(find . -name "*.proto" -exec grep -l protoc-gen-swagger {} \;) && \
        FILE=${FILE##*/} && FILE=${FILE%.*} && \
        cp $(find . -name $FILE.swagger.json) /swagger-ui/swagger.json && \
        sed -i "s|https://petstore.swagger.io/v2/swagger.json|./swagger.json|g" /swagger-ui/index.html && \
        sed -i "s|https://petstore.swagger.io/v2/swagger.json|./swagger.json|g" /swagger-ui/swagger-initializer.js && \
        go-bindata -o /build/swagger/swagger.go -nomemcopy -pkg=swagger -prefix "/swagger-ui/" /swagger-ui \
        ;fi
