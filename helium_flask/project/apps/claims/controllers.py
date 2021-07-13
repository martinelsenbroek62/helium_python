from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash


claim_router = Blueprint("claim_router", __name__)


@claim_router.route("reimburse/")
def reimburse():
    return jsonify([])


@claim_router.route("list/")
def list():
    return jsonify([])
