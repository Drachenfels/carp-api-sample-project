import python_schema

from carp_api import endpoint, exception


class BaseEndpoint(endpoint.BaseEndpoint):
    input_schema = None

    output_schema = None

    def parse_input_payload(self, payload):
        if not self.input_schema:
            return payload

        instance = self.input_schema()  # pylint: disable=not-callable

        try:
            instance.loads(payload)
        except python_schema.exception.PayloadError as err:
            raise exception.PayloadError(err)

        return instance

    def parse_output_payload(self, payload):
        if not self.output_schema:
            return payload

        instance = self.output_schema()  # pylint: disable=not-callable

        try:
            instance.loads(payload)

        except python_schema.exception.PayloadError as err:
            raise exception.ResponseContentError(err)

        return instance.dumps()
