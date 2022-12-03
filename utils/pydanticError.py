from functools import wraps
from flask import make_response, request, jsonify, json

def custom_error(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)

        if type(res) == tuple:

            return res
        else:
            
            err_json = res.get_json()

            # check if pydantic throws an error (if not continue normally)
            if (err_json is None) or ("validation_error" not in err_json):
                return res
            
            val_err = err_json["validation_error"]

            # this is the final response format
            if "body_params" in val_err:
                return jsonify({
                        "status": "error",
                        "field":val_err['body_params'][0]['loc'][0],
                        "message": val_err['body_params'][0]['msg']
                        # "field": sing_err["loc"][0]
                        }), 400
    return wrapper