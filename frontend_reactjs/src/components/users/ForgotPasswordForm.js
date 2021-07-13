import React from "react";
import {routes} from "../../project/Const";


export const ForgotPasswordForm = () => {
    return (
        <>
            <div className="card-body">
					<form>
					 	<div className="form-group">
					    	<label htmlFor="Email">Enter your email to receive a login link</label>
					    	<input type="text" className="form-control" id="Email" placeholder="Enter the Email"/>
					  	</div>
					  	
					</form>
					<button type="button" className="btn btn-primary">Submit</button> 
   				</div>
  			
        </>
    );
}
export const ForgotPasswordFormFooter = () => {
    return (
            <a href={routes['login']} className="btn card-footer-anchor"><i className="fa fa-lock"></i>Back to login</a>
    )
}