import React from 'react';
import {ProfileHeading} from "../layout/ProfileHeading";
import indexImg from "../../assets/images/index_img.JPG";
import {routes} from "../../project/Const"

export default function Home() {
    return (
        <div className="container">
            <ProfileHeading/>
            <div className="text-center my-2 mb-5">
                <div className="btn_div">
                    <a href={routes['surveys']} className="btn btn-success"><h4>Take your survey</h4></a>
                </div>
                <div className="row mt-5">
                    <div className="col-4"><img src={indexImg} width="350" alt="index img"/></div>
                    <div className="col">
                        <h1 className="mt-1 index_heading">Sustain 6 Reimbursable Benefits</h1>
                        <p className="lead">Transform your employees into sustainability champions at work, home and
                            beyond.</p>
                    </div>
                </div>
                <div className="details">
                    <h2>Your Benefits</h2>
                    <br/>
                    <h2>How to Spend</h2>
                    <p className="parh">Getting reimbursed is a simple, 3-step process:</p>
                    <ul className="list-group">
                        <li className="list-group-item parh">Make your qualifying purchase</li>
                        <li className="list-group-item parh">Submit <a href={routes['explore']}>the
                            reimbursement
                            form</a></li>
                        <li className="list-group-item parh">Receive your reimbursement, minus taxes, in your next
                            paycheck
                        </li>
                    </ul>
                    <h3 className="mt-4"> Questions? <a href="mailto:help@sustbenefits.com">Email us</a> or chat us.
                    </h3>
                </div>
            </div>
        </div>

    );
}
