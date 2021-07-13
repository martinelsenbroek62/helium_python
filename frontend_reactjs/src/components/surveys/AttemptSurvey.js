import React, {Component} from 'react';
import {ProfileHeading} from "../layout/ProfileHeading"
import axios from "axios";
import {get_token} from "../../utilities/auth";
import StartSurveyPages from "../../pages/StartSurveyPages";
import {routes} from "../../project/Const";

const DynamicFields = (props) => {

    switch (props.type) {
        case "text":
            return (
                <div className="row d-flex justify-content-center">
                    <div className="form-group col-md-4">
                        <input className="form-control" id={props.id}
                               value={props.value}
                               placeholder={props.value}
                               onChange={props.callb}
                        />
                    </div>
                </div>
            );
        case "dropdown":
            return (
                <div>
                    <div className="row d-flex justify-content-center">
                        <div className="form-group col-md-4">
                            <select className="form-control" id={props.id}
                                    value={props.value}
                                    onChange={props.callb}
                            >
                                <option value="">-- Please Choose</option>
                                {props.options.map((n, j) => (
                                    <option value={n} key={j}>{n}</option>
                                ))}
                            </select>
                        </div>
                    </div>
                </div>
            );
    }
}

export class AttemptSurvey extends Component {
    constructor(props) {
        super(props);
        this.state = {
            group_id: null,
            token_str: get_token(),
            content: {
                category: null,
                group: null,
            },
            questions: [],
            answers: {},
            survey_ended: false
        }
        this.handleInputChange = this.handleInputChange.bind(this)
        this.nextButton = this.nextButton.bind(this)
        this.previousButton = this.previousButton.bind(this)
    }

    render() {
        if (this.state.survey_ended) {
            return <StartSurveyPages redirected={true}/>
        } else {
            return (
                <div className="container my-2">
                    <ProfileHeading/>
                    <div className="text-center mt-3 mb-3 nbutton ">
                        <button type="button" className="btn btn-secondary b1">Home</button>
                        <button type="button" className="btn btn-secondary b2">Sections</button>
                        <button type="button" className="btn btn-secondary b3">Report</button>
                        <button type="button" className="btn btn-secondary b4">Data</button>
                        <button type="button" className="btn btn-secondary b5">FQA</button>
                    </div>
                    <div className="c1 mb-3 mt-3 d-flex p-2">
                        <button className="btn btn-primary prev d-inline" onClick={this.previousButton}
                        ><i className="fa fa-caret-left" aria-hidden="true"/> Prev
                        </button>
                        <h3 className=" text-center  h31 ">{this.state.content.category}: {this.state.content.group}</h3>
                        <button className="btn btn-primary next d-inline"
                                onClick={this.nextButton}
                        >Next <i className="fa fa-caret-right" aria-hidden="true"/></button>
                    </div>
                    <form>
                        <div>
                            {(this.state.questions.length !== 0) && this.state.questions.map((item, i) => (
                                <div key={i}>
                                    <div className="container h4 mt-5 mb-2 text-center ">
                                        <span className="text-danger">*</span> {item.label}
                                    </div>
                                    <div className="container mb-3 mt-4 text-center state-list h4">
                                        <DynamicFields type={item.type} options={item.choices} value={item.value}
                                                       id={item.id} f_index={i} callb={this.handleInputChange}/>

                                    </div>
                                </div>
                            ))}
                        </div>
                    </form>
                    <div className="container text-center mt-3 mb-3">
                        <button className="btn btn-primary" onClick={this.nextButton}><span
                            className="h5">Save &amp; Continue</span></button>
                    </div>
                    <a href={routes['surveys']}>
                        <p className="muted text-center">
                            Return to end of survey
                        </p></a>
                </div>
            )
        }
    }

    componentDidMount() {
        axios(
            {
                url: `http://127.0.0.1:5000/current_group/`,
                method: "get",
                headers: {'Authorization': this.state.token_str}
            }).then(
            response => {
                console.log(response);
                this.setStateFromResponse(response);
            }
        ).catch(
            error => {
                console.log(error);
                console.log("exception caught!")
            })
    }

    handleInputChange = (event) => {
        let answers = this.state.answers
        answers[event.target.id] = event.target.value
        this.setState({answers: answers})
        let questions = this.state.questions
        var found = -1;
        for (var i = 0; i < questions.length; i++) {
            if (questions[i].id == event.target.id) {
                found = i;
                break;
            }
        }
        if (found !== -1) {
            questions[found].value = event.target.value
            this.setState({questions: questions})
        }

    }

    setStateFromResponse(response) {
        this.setState({
            content: {
                category: response.data.category_name,
                group: response.data.group_name,
            }
        })
        this.setState({
            questions: response.data.questions
        })
        this.setState({
            group_id: response.data.group_id
        })
    }

    nextButton() {
        axios(
            {
                url: `http://127.0.0.1:5000/groups/${this.state.group_id}/next/`,
                method: "post",
                data: {answers: this.state.answers},
                headers: {'Authorization': this.state.token_str}
            }).then(
            response => {
                console.log(response);
                if ("message" in response.data) {
                    this.setState({survey_ended: true})
                    return
                }
                this.setStateFromResponse(response);
                this.setState({answers: {}})
            }
        ).catch(
            error => {
                console.log(error);
                console.log("exception caught!")
            })
    }

    previousButton() {
        axios(
            {
                url: `http://127.0.0.1:5000/groups/${this.state.group_id}/back/`,
                method: "post",
                data: {answers: this.state.answers},
                headers: {'Authorization': this.state.token_str}
            }).then(
            response => {
                console.log(response);
                if ("message" in response.data) {
                    this.setState({survey_ended: true})
                    return
                }
                this.setStateFromResponse(response);
                this.setState({answers: {}})
            }
        ).catch(
            error => {
                console.log(error);
                console.log("exception caught!")
            })
    }

}
