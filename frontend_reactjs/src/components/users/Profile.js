import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';
import {ProfileHeading} from '../layout/ProfileHeading';
import axios from "axios";
import {authFetch, useAuth} from "../../utilities/auth";


export class Profile extends Component {
    constructor(props) {
        super(props);
        this.state = {
            user_info: {
                email: "",
                password: "",
                name: ""
            },
            updated_info: {},
            token_str: "Bearer " + localStorage.getItem("REACT_TOKEN_AUTH_KEY").replaceAll('"', '')
        }
        this.handleInputChange = this.handleInputChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }


    handleInputChange(event) {
        let u_info = this.state.user_info
        u_info[event.target.id] = event.target.value
        this.setState({user_info: u_info})
    }

    handleSubmit(event) {
        axios(
            {
                url: "http://127.0.0.1:5000/profile/",
                method: "post",
                data: this.state.user_info,
                headers: {'Authorization': this.state.token_str}
            }).then(
            response => {
                console.log(response);
                console.log("authorization for get request!")
            }
        ).catch(
            error => {
                console.log(error);
                console.log("exception caught!")
            })
    }

    componentDidMount() {
        console.log('component mounted');
        axios(
            {
                url: "http://127.0.0.1:5000/profile/",
                method: "get",
                headers: {'Authorization': this.state.token_str}
            }).then(
            response => {
                console.log(response);
                console.log("authorization for get request!")
                let u_info = {
                    email: response.data.email,
                    name: response.data.name
                }
                this.setState({user_info: u_info})
            }
        ).catch(
            error => {
                console.log(error);
                console.log("exception caught!")
            })
    }

    render() {
        return (
            <div className="container mb-5 pb-5" style={{marginBottom: '200 !important'}}>
                <ProfileHeading/>
                <form>
                    <div className="form-group">
                        <label htmlFor="email">Name</label>
                        <input type="text" className="form-control" id="name" onChange={this.handleInputChange}
                               value={this.state.user_info.name}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="email">Email</label>
                        <input type="text" className="form-control" id="email" onChange={this.handleInputChange}
                               value={this.state.user_info.email}/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" className="form-control" id="password" onChange={this.handleInputChange}
                               value={this.state.user_info.password}/>
                    </div>

                    <button type="submit" className="btn btn-primary" onClick={this.handleSubmit}>Update</button>
                </form>
            </div>

        );
    }
}
