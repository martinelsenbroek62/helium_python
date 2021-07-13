import React from "react";
import {NavLink} from "react-router-dom";
import Logo from "../../assets/images/logo.png";
import {routes} from "../../project/Const";

export default function NavBar() {
     return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary navbar-inverse" id="benefits_menu">
            <NavLink className="navbar-brand no_padding" to={routes['home']}>
                <img src={Logo} width="225" alt="nav logo"/>
            </NavLink>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item">
                        <NavLink className="nav-link" to={routes['home']}>
                            <i className="fa fa-home"/>Home</NavLink>
                    </li>

                    <li className="nav-item">
                        <NavLink className="nav-link" to={routes['explore']}>
                            <i className="fa fa-compass"></i>
                            Explore Benefits</NavLink>
                    </li>


                    <li className="nav-item">
                        <NavLink className="nav-link" to={routes['claims']}>
                            <i className="fa fa-briefcase"></i>
                            My Claims</NavLink>
                    </li>

                    <li className="nav-item">
                        <NavLink className="nav-link" to={routes['surveys']}>
                            <i className="fa fa-list"></i>
                            My Surveys</NavLink>
                    </li>

                    <li className="nav-item">
                        <NavLink className="nav-link" to={routes['report']} target="_self">
                            <i className="fa fa-globe"></i>
                            My Footprint</NavLink>
                    </li>
                </ul>

                <ul className="nav navbar-nav ml-auto">

                    <li className="nav-item">
                        <NavLink className="nav-link" to="https://intercom.help/sustainabilitybenefits/" target="_blank">
                            <i className="fa fa-question-circle"></i>
                            Help Center</NavLink>
                    </li>

                    <li className="nav-item">
                        <NavLink className="nav-link" to={routes['profile']}><i className="fa fa-user"/> My Profile</NavLink>
                    </li>

                    <li className="nav-item">
                        <NavLink className="nav-link" to={routes['logout']}>
                            <i className="fa fa-lock"/>
                            Logout</NavLink>
                    </li>
                </ul>
                <div className="searchbar">

                </div>
            </div>
        </nav>
    );
}