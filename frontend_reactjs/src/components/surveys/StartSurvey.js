import React from 'react';
import {NavLink} from 'react-router-dom';
import {routes} from "../../project/Const";

export const StartSurvey = () => {
    return (
        <div className="container my-2">
            <div className="text-center">
                <h1 className="survey_heading">Let's Get Started</h1>
                <p className="survey_parh">Welcome to the 2021 Sustain 6 Demo Survey! We use this to measure your
                    household's impact and help us measure our progress toward reaching our carbon reduction goals. By
                    taking the survey, you'll get a report to help you with your own personal goals. All your survey
                    information will be kept confidential</p>
            </div>
            <div className="card-deck">
                <div className="card">
                    <div className="card-body">
                        <h4 className="card-title text-center">What You'll Get</h4>
                        <p className="card_awesome"><span className="fa-stack fa-lg fontawesome">
            <i className="fa fa-circle fa-stack-2x gold"/>
            <i className="fa fa-camera fa-stack-1x fa-inverse"/>
          </span> A clear picture of your carbon footprint</p>
                        <p className="card_awesome"><span className="fa-stack fa-lg fontawesome">
            <i className="fa fa-circle fa-stack-2x gold"/>
            <i className="fa fa-bullhorn fa-stack-1x fa-inverse"/>
          </span> How your carbon footprint compares with others</p>
                        <p className="card_awesome"><span className="fa-stack fa-lg fontawesome">
            <i className="fa fa-circle fa-stack-2x gold"/>
            <i className="fa fa-lightbulb-o fa-stack-1x fa-inverse"/>
          </span> Ideas of how to decrease your carbon impact</p>
                    </div>
                </div>
                <div className="card">
                    <div className="card-body">
                        <h4 className="card-title text-center">How much time does it take?</h4>
                        <p className="card_awesome"><span className="fa-stack fa-lg fontawesome">
            <i className="fa fa-circle fa-stack-2x gold"/>
            <i className="fa fa-clock-o fa-stack-1x fa-inverse"/>
          </span> 10-15 minutes</p>
                        <h4 className="card-title text-center">What you'll need</h4>
                        <p className="card_awesome"><span className="fa-stack fa-lg fontawesome">
            <i className="fa fa-circle fa-stack-2x gold"/>
            <i className="fa fa-clipboard fa-stack-1x fa-inverse"/>
          </span> Last year's info on vehicles, utility & fuel usage</p>
                    </div>
                </div>

            </div>

            <h5 className="text-center mb-5 mt-2">Please complete the survey by the deadline of </h5>
            <div className="text-center mt-5 mb-3">
                <NavLink to={routes['attempt_survey']} className="btn btn-primary"><h5>Start Survey</h5></NavLink>

            </div>
            <a href={routes['attempt_survey']}>
            <p className="text-center survey_link"><>Continue where you left off <i className="fa fa-arrow-right"/></>
            </p></a>
        </div>
    );
}
