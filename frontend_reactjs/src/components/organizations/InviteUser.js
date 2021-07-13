import React from "react";
import Logo from "../../assets/images/login.jpg";


export default function InviteUser() {
    return (
        <div className="organization-login-invite-user">
            <div className="img-div mb-3 mt-5"><img src={Logo} width="300" /></div>
            <div className="maincenter ">
                <div className="card marginauto">
                    <div className="card-body ">

                        <p className="card-text textp"><b>Sustain 6</b> requires a password for self registration.
                            If you do not know the password please talk to your employer.</p>
                        <label className="lab">Enter Organization Password*</label>
                        <input type="text" name="something" className="form-control mb-3" />
                            <button className="btn btn-primary">Continue <i className="fa fa-send"/></button>
                    </div>

                </div>
            </div>

        </div>
    )
}