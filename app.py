from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='public')

# 파일 경로 설정
valid_numbers_file = os.path.join(app.static_folder, 'validElectionNumbers.json')
used_numbers_file = os.path.join(app.static_folder, 'usedElectionNumbers.json')
users_file = os.path.join(app.static_folder, 'users.json')
votes_file = os.path.join(app.static_folder, 'votes.json')
candidates_file = os.path.join(app.static_folder, 'candidates.json')

# JSON 파일 읽기 함수
def read_json_file(file_path, default_data):
    if not os.path.exists(file_path):
        write_json_file(file_path, default_data)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_data

# JSON 파일 쓰기 함수
def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 기본 데이터 설정
default_candidates_data = {
    "candidates": [
        {"id": "candidate1", "number": 1, "name": "김철수"},
        {"id": "candidate2", "number": 2, "name": "이영희"},
        {"id": "candidate3", "number": 3, "name": "박민수"},
        {"id": "candidate4", "number": 4, "name": "정지훈"},
        {"id": "candidate5", "number": 5, "name": "최민호"},
        {"id": "candidate6", "number": 6, "name": "한지민"},
        {"id": "candidate7", "number": 7, "name": "강동원"},
        {"id": "candidate8", "number": 8, "name": "송중기"},
        {"id": "candidate9", "number": 9, "name": "배수지"},
        {"id": "candidate10", "number": 10, "name": "오하늬"},
        {"id": "candidate11", "number": 11, "name": "김태리"},
        {"id": "candidate12", "number": 12, "name": "유아인"},
        {"id": "candidate13", "number": 1, "name": "이성민"},
        {"id": "candidate14", "number": 2, "name": "조정석"},
        {"id": "candidate15", "number": 3, "name": "강소라"},
        {"id": "candidate16", "number": 4, "name": "박보검"},
        {"id": "candidate17", "number": 5, "name": "유재석"},
        {"id": "candidate18", "number": 6, "name": "이광수"},
        {"id": "candidate19", "number": 7, "name": "김고은"},
        {"id": "candidate20", "number": 8, "name": "전지현"},
        {"id": "candidate21", "number": 9, "name": "이병헌"},
        {"id": "candidate22", "number": 10, "name": "고두심"},
        {"id": "candidate23", "number": 11, "name": "김혜수"},
        {"id": "candidate24", "number": 12, "name": "정우성"},
        {"id": "candidate25", "number": 13, "name": "신민아"},
        {"id": "candidate26", "number": 14, "name": "김지원"},
        {"id": "candidate27", "number": 15, "name": "김명민"},
        {"id": "candidate28", "number": 16, "name": "조진웅"},
        {"id": "candidate29", "number": 17, "name": "김희애"},
        {"id": "candidate30", "number": 18, "name": "공유"},
        {"id": "candidate31", "number": 19, "name": "한석규"},
        {"id": "candidate32", "number": 20, "name": "유해진"},
        {"id": "candidate33", "number": 21, "name": "송혜교"},
        {"id": "candidate34", "number": 22, "name": "차승원"},
        {"id": "candidate35", "number": 23, "name": "손예진"},
        {"id": "candidate36", "number": 24, "name": "김수현"},
        {"id": "candidate37", "number": 25, "name": "박신혜"},
        {"id": "candidate38", "number": 26, "name": "김준호"},
        {"id": "candidate39", "number": 27, "name": "신동엽"},
        {"id": "candidate40", "number": 28, "name": "차태현"},
        {"id": "candidate41", "number": 29, "name": "윤여정"},
        {"id": "candidate42", "number": 30, "name": "김상중"},
        {"id": "candidate43", "number": 31, "name": "임시완"},
        {"id": "candidate44", "number": 32, "name": "이준기"},
        {"id": "candidate45", "number": 33, "name": "박서준"},
        {"id": "candidate46", "number": 34, "name": "한지민"},
        {"id": "candidate47", "number": 35, "name": "수지"},
        {"id": "candidate48", "number": 36, "name": "장혁"},
        {"id": "candidate49", "number": 1, "name": "정우"},
        {"id": "candidate50", "number": 2, "name": "정경호"},
        {"id": "candidate51", "number": 3, "name": "김성균"},
        {"id": "candidate52", "number": 4, "name": "손현주"},
        {"id": "candidate53", "number": 5, "name": "신하균"},
        {"id": "candidate54", "number": 6, "name": "정소민"},
        {"id": "candidate55", "number": 7, "name": "김민희"},
        {"id": "candidate56", "number": 8, "name": "오연서"},
        {"id": "candidate57", "number": 9, "name": "박해준"},
        {"id": "candidate58", "number": 10, "name": "박명수"},
        {"id": "candidate59", "number": 11, "name": "박보영"},
        {"id": "candidate60", "number": 12, "name": "안재홍"},
        {"id": "candidate61", "number": 13, "name": "류준열"},
        {"id": "candidate62", "number": 14, "name": "김동욱"},
        {"id": "candidate63", "number": 15, "name": "유연석"},
        {"id": "candidate64", "number": 16, "name": "박서현"},
        {"id": "candidate65", "number": 17, "name": "남궁민"},
        {"id": "candidate66", "number": 18, "name": "전소민"},
        {"id": "candidate67", "number": 19, "name": "김유정"},
        {"id": "candidate68", "number": 20, "name": "서강준"},
        {"id": "candidate69", "number": 21, "name": "윤계상"},
        {"id": "candidate70", "number": 22, "name": "이성경"},
        {"id": "candidate71", "number": 23, "name": "남주혁"},
        {"id": "candidate72", "number": 24, "name": "한효주"}
    ]
}
default_valid_numbers_data = {"numbers": ["123456", "654321"]}  # 유효한 선거번호 예시
default_used_numbers_data = []
default_users_data = []
default_votes_data = []

# 서버 시작 시 기본 데이터 파일 생성
def initialize_files():
    read_json_file(valid_numbers_file, default_valid_numbers_data)
    read_json_file(used_numbers_file, default_used_numbers_data)
    read_json_file(users_file, default_users_data)
    read_json_file(votes_file, default_votes_data)
    read_json_file(candidates_file, default_candidates_data)

initialize_files()

@app.route('/validElectionNumbers', methods=['GET'])
def get_valid_numbers():
    try:
        data = read_json_file(valid_numbers_file, {"numbers": []})
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    election_number = request.json.get('electionNumber')
    try:
        valid_numbers = read_json_file(valid_numbers_file, {"numbers": []})
        used_numbers = read_json_file(used_numbers_file, [])

        if election_number in used_numbers:
            return jsonify(success=False, message='이미 투표에 참여하셨습니다.')
        elif election_number in valid_numbers['numbers']:
            return jsonify(success=True)
        else:
            return jsonify(success=False, message='잘못된 선거번호입니다.')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/vote', methods=['POST'])
def vote():
    election_number = request.json.get('electionNumber')
    votes = request.json.get('votes')
    set_number = request.json.get('setNumber')
    try:
        votes_data = read_json_file(votes_file, [])

        user_votes = next((user for user in votes_data if user['electionNumber'] == election_number), None)
        if not user_votes:
            user_votes = { 'electionNumber': election_number, 'votes': {} }
            votes_data.append(user_votes)

        candidates_data = read_json_file(candidates_file, {"candidates": []})
        candidates_dict = {candidate['name']: candidate['id'] for candidate in candidates_data['candidates']}
        standardized_votes = [candidates_dict.get(vote, vote) for vote in votes]

        user_votes['votes'][str(set_number)] = standardized_votes

        if len(user_votes['votes']) == 3:
            used_numbers = read_json_file(used_numbers_file, [])
            users = read_json_file(users_file, [])
            users.append(election_number)
            used_numbers.append(election_number)

            write_json_file(users_file, users)
            write_json_file(used_numbers_file, used_numbers)

        write_json_file(votes_file, votes_data)

        return jsonify(success=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/verify', methods=['GET'])
def verify():
    election_number = request.args.get('electionNumber')
    try:
        votes_data = read_json_file(votes_file, [])
        user_votes = next((user for user in votes_data if user['electionNumber'] == election_number), None)
        if user_votes:
            return jsonify(user_votes['votes'])
        else:
            return jsonify({}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cancel', methods=['POST'])
def cancel_vote():
    election_number = request.json.get('electionNumber')
    try:
        votes_data = read_json_file(votes_file, [])
        used_numbers = read_json_file(used_numbers_file, [])
        users = read_json_file(users_file, [])

        user_votes = next((user for user in votes_data if user['electionNumber'] == election_number), None)
        if not user_votes:
            return jsonify(success=False, message='투표 정보가 없습니다.')

        votes_data = [vote for vote in votes_data if vote['electionNumber'] != election_number]
        used_numbers = [num for num in used_numbers if num != election_number]
        users = [num for num in users if num != election_number]

        write_json_file(votes_file, votes_data)
        write_json_file(used_numbers_file, used_numbers)
        write_json_file(users_file, users)

        return jsonify(success=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/progress', methods=['GET'])
def get_progress():
    try:
        users = read_json_file(users_file, [])
        valid_numbers = read_json_file(valid_numbers_file, {"numbers": []})
        total_voters = len(valid_numbers['numbers'])
        voted_count = len(users)

        return jsonify({
            'total': total_voters,
            'voted': voted_count
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/results', methods=['GET'])
def get_results():
    try:
        votes_data = read_json_file(votes_file, [])
        candidates_data = read_json_file(candidates_file, {"candidates": []})
        candidates_dict = {candidate['id']: candidate for candidate in candidates_data['candidates']}
        results = {'set1': [], 'set2': [], 'set3': []}

        for vote in votes_data:
            for set_number, candidates in vote['votes'].items():
                if set_number == '1':
                    for candidate in candidates:
                        update_results(results['set1'], candidate, candidates_dict)
                elif set_number == '2':
                    for candidate in candidates:
                        update_results(results['set2'], candidate, candidates_dict)
                elif set_number == '3':
                    for candidate in candidates:
                        update_results(results['set3'], candidate, candidates_dict)

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_results(results_set, candidate_id, candidates_dict):
    candidate = candidates_dict.get(candidate_id, {'number': '', 'name': candidate_id, 'id': candidate_id})
    candidate_name = candidate['name']
    # 일관된 이름 형식으로 변환
    if candidate['number']:
        candidate_name = f"기호 {candidate['number']}번: {candidate['name']}"
    for item in results_set:
        if item['id'] == candidate['id'] or item['name'] == candidate_name:
            item['votes'] += 1
            return
    results_set.append({'id': candidate['id'], 'number': candidate['number'], 'name': candidate_name, 'votes': 1})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(port=3000)
