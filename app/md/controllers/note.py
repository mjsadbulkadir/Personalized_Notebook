from flask import jsonify, request, session
from flask_restful import Resource
from app import db
from app.auth.decorators import token_required
from app.exception import PGAPIException
from app.md.models import Note, NotesSchema

class NoteView(Resource):

    @token_required
    def get(self):
        # print("FDSFDSDSVDSVDSVDVDFVDFVFDDF")
        notes = Note.query.filter_by(user_id=session['user_id']).all()
        print("debug=------------->",notes)
        notes_data = NotesSchema(many=True).dump(notes)
        return jsonify(notes_data)

    @token_required
    def post(self):
        note_data = request.get_json()
        # print("FDSFDSDSVDSVDSVDVDFVDFVFDDF--------------------1",note_data)
        if not note_data or 'note' not in note_data or len(note_data['note']) < 1:
            # print("FDSFDSDSVDSVDSVDVDFVDFVFDDF--------------------2")
            return jsonify({"error": "Note is too short!"})
        else:
            new_note = Note(data=note_data['note'], user_id=note_data['user_id'])
            db.session.add(new_note)
            db.session.commit()
            return NotesSchema().dump(new_note), 201

    @token_required
    def delete(self):
        data = request.get_json()
        note_id = data.get("id")
        if not note_id:
            return jsonify({"error": "Note ID is required"}), 400
        note = Note.query.get(note_id)
        if not note:
            return jsonify({"error": "Note not found"}), 404
        db.session.delete(note)
        db.session.commit()
        return jsonify({"message": "Note deleted"}), 200

    @token_required   
    def put(self):
        data = request.get_json()
        note_id = data.get("id")
        if not note_id:
            return jsonify({"error": "Note ID is required"}),
