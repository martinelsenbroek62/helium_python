import React, {Component} from "react";
import NavBar from "../components/layout/NavBar"
import {Footer} from "../components/layout/Footer";
import {StartSurvey} from "../components/surveys/StartSurvey";
import {ReportReady} from "../components/surveys/ReportReady";
import axios from "axios";
import {get_token} from "../utilities/auth";

export default class StartSurveyPages extends Component {
    constructor(props) {
        super(props);
        this.state = {
            has_reports: null,
            token: get_token()
        }
    }

    componentDidMount() {
        axios(
            {
                url: "http://127.0.0.1:5000/surveys/",
                method: "get",
                headers: {'Authorization': this.state.token}
            }).then(
            response => {
                console.log(response);
                this.setState({has_reports: response.data.has_reports});
            }
        ).catch(
            error => {
                console.log(error);
            })
    }

    render() {
        if (this.props.redirected) {
            return (
                <>
                    {this.state.has_reports ? <ReportReady/> :
                        <StartSurvey/>}
                </>
            )
        } else {
            return (
                <>
                    <NavBar/>
                    {this.state.has_reports ? <ReportReady/> :
                        <StartSurvey/>}
                    <Footer/>
                </>
            );
        }
    }
}