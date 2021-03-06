import {
  HttpErrorResponse,
  HttpEvent, HttpHandler, HttpInterceptor, HttpRequest, HttpResponse
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Injectable()
export class LoginInterceptor implements HttpInterceptor {

  constructor(private cookie: CookieService, private route: Router) { }

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<any>> {

    // If we have a token, we set it to the header Authorization:Token
    if (this.cookie.check('tkn')) {
      request = request.clone({
        setHeaders: {
          Authorization: `Token ${this.cookie.get('tkn')}`,
        }
      });
      // console.debug(request);
    } else {
      // request = request;
      this.route.navigateByUrl('/login');
    }

    return next.handle(request).pipe(
      // map((event: HttpEvent<any>) => {
      // if (event instanceof HttpResponse) {
      // console.log("letting pass in interceptor");
      // console.log("interceptor event: \n", event);
      // }
      // return event;
      // }),
      catchError((error: HttpErrorResponse) => {
        let data = {};
        data = {
          reason: error && error.error && error.error.reason ? error.error.reason : '',
          status: error.status
        };
        // console.log("Error catched by interceptor\n", data);
        return throwError(error);
      })
    )
  }
}

