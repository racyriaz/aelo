import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { environment } from './../../../environments/environment';
import { $login_resp, ApisService } from '../services/apis.service';
export interface $reg_err_response {
    fullname?: string | any;
    email?: string | any;
    username?: string | any;
    mobile?: string | any;
    password?: string | any;
}

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {


    loginFormElement = [
        { labelName: "User name", placeholder: "", iconName: "email", type: "text", fcName: "username", autocomplete: "on" },
        { labelName: "Password", placeholder: "", iconName: "password", type: "password", fcName: "password", autocomplete: "current-password" },
    ];
    regFormElement = [
        { labelName: "Full name", placeholder: "", iconName: "account_circle", type: "text", fcName: "full_name", autocomplete: "on" },
        { labelName: "Email", placeholder: "", iconName: "mail", type: "email", fcName: "email", autocomplete: "on" },
        { labelName: "User name", placeholder: "", iconName: "3p", type: "text", fcName: "username", autocomplete: "on" },
        { labelName: "Mobile number", placeholder: "", iconName: "call", type: "tel", fcName: "mobile", autocomplete: "on" },
        { labelName: "Password", placeholder: "", iconName: "password", type: "password", fcName: "password", autocomplete: "new-password" },
        { labelName: "Confirm password", placeholder: "", iconName: "password", type: "text", fcName: "confirm_password", autocomplete: "on" },
    ];

    newUser = true;
    url = "";

    focusOn: string | null = null;

    loginForm = new FormGroup({
        username: new FormControl(null, [Validators.required]),
        password: new FormControl(null, [Validators.required]),
    });
    registrationForm = new FormGroup({
        full_name: new FormControl(null, [Validators.required]),
        username: new FormControl(null, [Validators.required]),
        email: new FormControl(null, [Validators.required, Validators.email]),
        mobile: new FormControl(""),
        password: new FormControl(null, [Validators.required, Validators.minLength(8)]),
        confirm_password: new FormControl(null, [Validators.required, Validators.minLength(8)]),
    });

    constructor(public http: HttpClient, private cookie: CookieService, private route: Router, private api: ApisService) {

        // this.cookie.delete('tkn');
        // console.log("deleted token");
    }

    callFocus(val: any) {
        this.focusOn = val.path[0].id;
    }

    ngOnInit() {

    }

    submission: null | string | $reg_err_response | any = null;


    // Form submit
    register_user() {
        if (this.registrationForm.value.password === this.registrationForm.value.confirm_password) {
            this.api.registerUser(this.registrationForm.value).subscribe(
                (next) => {
                    this.submission = "success";
                    window.alert("User registered sucessfully! Please login to continue");
                    this.switchForms();
                },
                (err) => {
                    // console.log("what is this: ", err);
                    window.alert(err.error);
                    this.submission = err.error;
                    this.registrationForm.setErrors(err.error);
                }
            );
        } else {
            this.submission = "failed"
            this.registrationForm.setErrors({ confirm_password: "Password matching failed!" });
        };
    }

    login_user() {
        this.api.loginUser(this.loginForm.value).subscribe(
            (next: $login_resp) => {
                this.submission = "success";
                this.cookie.set('tkn', next.token);
                this.cookie.set('username', next.username);
                // console.log(next);
                this.route.navigateByUrl('/transaction')
            },
            (err) => {
                // console.log("what is this: ", err);
                window.alert(err.error);
                this.submission = err.error;
                this.loginForm.setErrors(err.error);
            }
        );
    }

    switchForms() {
        this.newUser = !this.newUser;
        // console.log(this.newUser);
    }
}

export function export_form_data(val: { username: string, password: string, fullname: string, email: string }) {
    const formData = new FormData();
    for (const [key, value] of Object.entries(val)) {
        formData.append(key, value);
        // console.log(key, value);
    }
    return formData;
}
