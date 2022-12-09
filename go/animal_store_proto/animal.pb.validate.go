// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: animal_store_proto/animal.proto

package animal_store_proto

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/golang/protobuf/ptypes"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = ptypes.DynamicAny{}
)

// define the regex for a UUID once up-front
var _animal_uuidPattern = regexp.MustCompile("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

// Validate checks the field values on AnimalReq with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *AnimalReq) Validate() error {
	if m == nil {
		return nil
	}

	if utf8.RuneCountInString(m.GetAnimalId()) < 1 {
		return AnimalReqValidationError{
			field:  "AnimalId",
			reason: "value length must be at least 1 runes",
		}
	}

	return nil
}

// AnimalReqValidationError is the validation error returned by
// AnimalReq.Validate if the designated constraints aren't met.
type AnimalReqValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AnimalReqValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AnimalReqValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AnimalReqValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AnimalReqValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AnimalReqValidationError) ErrorName() string { return "AnimalReqValidationError" }

// Error satisfies the builtin error interface
func (e AnimalReqValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAnimalReq.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AnimalReqValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AnimalReqValidationError{}

// Validate checks the field values on AnimalRsp with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *AnimalRsp) Validate() error {
	if m == nil {
		return nil
	}

	if v, ok := interface{}(m.GetAnimalId()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AnimalRspValidationError{
				field:  "AnimalId",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if v, ok := interface{}(m.GetAnimal()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AnimalRspValidationError{
				field:  "Animal",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if v, ok := interface{}(m.GetPrice()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AnimalRspValidationError{
				field:  "Price",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// AnimalRspValidationError is the validation error returned by
// AnimalRsp.Validate if the designated constraints aren't met.
type AnimalRspValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AnimalRspValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AnimalRspValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AnimalRspValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AnimalRspValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AnimalRspValidationError) ErrorName() string { return "AnimalRspValidationError" }

// Error satisfies the builtin error interface
func (e AnimalRspValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAnimalRsp.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AnimalRspValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AnimalRspValidationError{}