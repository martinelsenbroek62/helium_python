import React from 'react';
import {routes} from "../../project/Const";
import axios from 'axios'
import {useHistory} from "react-router-dom";
import {login, logout, useAuth} from "../../utilities/auth"

export const LoginForm = (props) => {
    let creds = {"email": "", "password": ""};
    const history = useHistory();

    function handleInputChange(event) {
        creds[event.target.id] = event.target.value
    }

    function handleSubmit(event) {
        if (creds.password.value === undefined) {
            console.log("Password field is empty!");
        } else if (creds.email.value === undefined) {
            console.log("Email field is empty!");
        }
        axios({
            method: "post",
            url: "http://127.0.0.1:5000/login/",
            headers: {
                'Content-type': 'application/json'
            },
            data: creds,
        }).then(
            response => {
                console.log(response);
                login(response.data.access_token)
                history.push(routes['home'])
            }
        ).catch(
            error => {
                console.log(error);
                if (error.response.statusText === "UNAUTHORIZED") {
                    console.log("Wrong password/email!")
                }
            }
        );
        // if (creds['email'] == "akbarahmadshah1@gmail.com") {
        //     history.push(routes['home'])
        // }
    }

    const [logged] = useAuth();

    if (logged) {
        history.push(routes['home'])
    }
    return (
        <>
            <div className="card-body">
                <form>
                    <div className="form-group">
                        <label htmlFor="Email">Email</label>
                        <input type="text" className="form-control" id="email" placeholder="Enter the Email"
                               onChange={handleInputChange}/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="Password">Password</label>
                        <input type="Password" className="form-control" id="password" placeholder="Enter Password"
                               onChange={handleInputChange}/>
                    </div>
                    <button onClick={handleSubmit} type="button" className="btn btn-primary">Login <i
                        className="fa fa-paper-plane"/>
                    </button>
                </form>
            </div>
        </>
    );
}
export const LoginFormFooter = () => {
    return (
        <a href={routes['forgot_password']} className="btn card-footer-anchor"><i className="fa fa-lock"/> Forgot
            password?</a>
    )
}