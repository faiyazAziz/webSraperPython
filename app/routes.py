from flask import Blueprint, request, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/message', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('selectedElements', '')
    # print(message)

    # Process the message here (could involve more complex logic or function calls)
    response_message = f"Received: {message}"

    return jsonify({'response': response_message}), 200
