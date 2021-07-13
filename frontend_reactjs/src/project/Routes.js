import React from 'react';
import {Route, Switch, Redirect} from "react-router-dom";
import HomePage from "../pages/HomePage";
import {routes} from "./Const"
import ProfilePage from "../pages/ProfilePage";
import {Login} from "../pages/LoginPages";
import {LoginForm, LoginFormFooter} from "../components/users/LoginForm";
import {ForgotPasswordForm, ForgotPasswordFormFooter} from "../components/users/ForgotPasswordForm";
import StartSurveyPages from "../pages/StartSurveyPages";
import ClaimsPage from "../pages/ClaimsPage";
import ReimbursementFormPage from "../pages/ReimbursementFormPage";
import OrganizationFormPage from "../pages/OrganizationFormPage";
import InviteUserPage from "../pages/InviteUserPage";
import AttemptSurveyPage from "../pages/AttemptSurveyPage";
import {PrivateRoute} from "../utilities/PrivateRoute";

export const RoutesSwitcher = () => {
    return (
        <Switch>
            <Route exact path={routes['login']}>
                <Login form_type={<LoginForm/>} footer={<LoginFormFooter/>}/>
            </Route>
            <Route exact path={routes['forgot_password']}>
                <Login form_type={<ForgotPasswordForm/>} footer={<ForgotPasswordFormFooter/>}/>
            </Route>
            <Route exact path={routes['logout']}>
                <Login form_type={<LoginForm/>} footer={<LoginFormFooter/>} extra={"logout_first"}/>
            </Route>
            <PrivateRoute path={routes['home']} component={HomePage}/>
            <PrivateRoute path={routes['profile']} component={ProfilePage}/>

            <PrivateRoute path={routes['surveys']} component={StartSurveyPages}/>
            <PrivateRoute path={routes['claims']} component={ClaimsPage}/>
            <PrivateRoute path={routes['explore']} component={ReimbursementFormPage}/>
            <PrivateRoute path={routes['attempt_survey']} component={AttemptSurveyPage}/>
            <Route exact path={routes['organization_pass']} component={OrganizationFormPage}/>
            <Route exact path={routes['invite_user']} component={InviteUserPage}/>
            {/*<Route exact path={routes['report']}/>*/}
            <Redirect from='/' to={routes["login"]}/>

            {/*<Route path="/404" component={NotFound}/>*/}
            {/*<Redirect from='*' to='/404'/>*/}
        </Switch>
    );
}