import React from "react";
import {ProfileHeading} from "../layout/ProfileHeading";
import {routes} from "../../project/Const";

export const ReportReady = (props) => {
    return (
        <div className="container mb-5 pb-5" style={{marginBottom: '200px !important'}}>
            <ProfileHeading/>
            <div className="container text-center mb-4">
                <h1>Your Household Report is Ready!</h1>
            </div>
            <div className="text-center mb-3">
                <h3 className="center"><i className="fa fa-star text-warning"/>Find out what it means for you...<i
                    className="fa fa-star text-warning"/></h3>
            </div>
            <div className="text-center mb-5">
                Thank you for taking the 2021 Sustain 6 Demo Survey!
                <br/> Now you can explore the results!
            </div>
            <div className="text-center mb-5">
                <a href={routes['report']} className="btn btn-primary">
                    <i className="fa fa-caret-left"/> Go To Your Report <i className="fa fa-caret-right"/>
                </a>
            </div>
            <div className="text-center">
                <a target="_self" href={routes['attempt_survey']}>
                    Continue where you left off <i className="fa fa-arrow-right"/>
                </a>
            </div>
        </div>


    );

}