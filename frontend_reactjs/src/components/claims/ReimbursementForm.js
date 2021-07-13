import React from "react";
import {ProfileHeading} from "../layout/ProfileHeading";


export default function ReimbursementForm() {
    return (
        <div className="container mb-5 pb-5" style={{MarginBottom: '200px !important;'}}>
            <ProfileHeading />
            <div>
                <span>Submit a Claim</span>
                <ol className="Order_list">
                    <li>Select a Product Type below to start a claim</li>
                    <li>Complete and submit form with supporting documentation</li>
                    <li>Your claim will be reviewed within 3-5 business days</li>
                    <li>Once approved you will be reimbursed the following pay period</li>
                </ol>
            </div>
            <div className="">
                Search: <input type="text" id="filter_categories" value="" />
                <span className="">
                  <a href="?">
                    RESET
                  </a>
                </span>
            </div>
        </div>
)
}