import React from "react";
import {routes} from "../../project/Const";


export default function Claims() {
    return (
        <div className="container mb-5 pb-5" style={{marginBottom: '200px !important;'}}>
            <div className="Profile_heading">
                <h4>
                    Sustain 6
                </h4>
            </div>
            <div><h1>Your Claims History</h1></div>
            <div>
                <table className="table">
                    <thead>
                    <tr className="col_headings">
                        <th scope="col">Status</th>
                        <th scope="col">ID</th>
                        <th scope="col">Program</th>
                        <th scope="col">Category</th>
                        <th scope="col">Focus Area</th>
                        <th scope="col">Product</th>
                        <th scope="col">Date</th>
                        <th scope="col">Amount</th>
                    </tr>
                    </thead>
                </table>
            </div>
            <div><a className="btn btn-primary" href={routes['explore']}>
                Submit New Claim
            </a></div>
        </div>
    )
}