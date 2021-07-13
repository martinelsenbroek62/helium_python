import React from "react";
import Logo from "../../assets/images/login.jpg";
import {routes} from "../../project/Const";
import '../../assets/App.css';
import {ProfileHeading} from "../layout/ProfileHeading";



export default function OrganizationForm() {
    return (
        <>
            <div className="organization-login">
            <div className="mb-3 mt-5"><img src={Logo} alt="logo" width="300" /></div>
                <div className="card marginauto">
                    <div className="card inside p-3">
                        <label className="lab">Email</label>
                        <input type="text" name="something" className="form-control mb-3" />
                            <button className="btn btn-primary mb-2" style={{width: "150px;"}}>Create Survey<i
                                className="fa fa-send" /></button>
                    </div>
                    <div className="card-footer" style={{padding: "2 !important;"}}><a href={routes['forgot_password']}><i
                        className="fa fa-lock" style={{fontSize:"16px"}}/> Forget Password?</a></div>


                </div>
            </div>
        </>
    )
}