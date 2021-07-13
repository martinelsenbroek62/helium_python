import React from "react";
import loginImg from "../assets/images/login_logo.jpg";
import {logout} from "../utilities/auth";

export const Login = (props) => {

    if (props.extra === "logout_first") {
        logout();
    }
    return (
        <div className="container my-5 py-5">
            <div className="text-center mb-5">
                <img src={loginImg} width="300" alt="loginImg"/>
            </div>
            <div className="login_box">
                <div className="card">
                    <h1 className="card-header">Welcome to Sustainability Benefits</h1>
                    {props.form_type}
                    <div className="card-footer">
                        {props.footer}
                    </div>
                </div>
            </div>
        </div>
    );
}