from email.message import EmailMessage
from env import password
import ssl
import smtplib
from email_lists import email_receivers

email_sender = 'testaccount@gmail.com'
email_password = password

subject = 'Automated Cold Email Marketing Tool'
body = "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n<html data-editor-version=\"2\" class=\"sg-campaigns\" xmlns=\"http://www.w3.org/1999/xhtml\">\n    <head>\n      <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1\">\n      <!--[if !mso]><!-->\n      <meta http-equiv=\"X-UA-Compatible\" content=\"IE=Edge\">\n      <!--<![endif]-->\n      <!--[if (gte mso 9)|(IE)]>\n      <xml>\n        <o:OfficeDocumentSettings>\n          <o:AllowPNG/>\n          <o:PixelsPerInch>96</o:PixelsPerInch>\n        </o:OfficeDocumentSettings>\n      </xml>\n      <![endif]-->\n      <!--[if (gte mso 9)|(IE)]>\n  <style type=\"text/css\">\n    body {width: 600px;margin: 0 auto;}\n    table {border-collapse: collapse;}\n    table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;}\n    img {-ms-interpolation-mode: bicubic;}\n  </style>\n<![endif]-->\n      <style type=\"text/css\">\n    body, p, div {\n      font-family: verdana,geneva,sans-serif;\n      font-size: 16px;\n    }\n    body {\n      color: #516775;\n    }\n    body a {\n      color: #993300;\n      text-decoration: none;\n    }\n    p { margin: 0; padding: 0; }\n    table.wrapper {\n      width:100% !important;\n      table-layout: fixed;\n      -webkit-font-smoothing: antialiased;\n      -webkit-text-size-adjust: 100%;\n      -moz-text-size-adjust: 100%;\n      -ms-text-size-adjust: 100%;\n    }\n    img.max-width {\n      max-width: 100% !important;\n    }\n    .column.of-2 {\n      width: 50%;\n    }\n    .column.of-3 {\n      width: 33.333%;\n    }\n    .column.of-4 {\n      width: 25%;\n    }\n    @media screen and (max-width:480px) {\n      .preheader .rightColumnContent,\n      .footer .rightColumnContent {\n        text-align: left !important;\n      }\n      .preheader .rightColumnContent div,\n      .preheader .rightColumnContent span,\n      .footer .rightColumnContent div,\n      .footer .rightColumnContent span {\n        text-align: left !important;\n      }\n      .preheader .rightColumnContent,\n      .preheader .leftColumnContent {\n        font-size: 80% !important;\n        padding: 5px 0;\n      }\n      table.wrapper-mobile {\n        width: 100% !important;\n        table-layout: fixed;\n      }\n      img.max-width {\n        height: auto !important;\n        max-width: 100% !important;\n      }\n      a.bulletproof-button {\n        display: block !important;\n        width: auto !important;\n        font-size: 80%;\n        padding-left: 0 !important;\n        padding-right: 0 !important;\n      }\n      .columns {\n        width: 100% !important;\n      }\n      .column {\n        display: block !important;\n        width: 100% !important;\n        padding-left: 0 !important;\n        padding-right: 0 !important;\n        margin-left: 0 !important;\n        margin-right: 0 !important;\n      }\n      .social-icon-column {\n        display: inline-block !important;\n      }\n    }\n  </style>\n      <!--user entered Head Start-->\n\n     <!--End Head user entered-->\n    </head>\n    <body>\n      <center class=\"wrapper\" data-link-color=\"#993300\" data-body-style=\"font-size:16px; font-family:verdana,geneva,sans-serif; color:#516775; background-color:#ffffff;\">\n        <div class=\"webkit\">\n          <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" width=\"100%\" class=\"wrapper\" bgcolor=\"#ffffff\">\n            <tr>\n              <td valign=\"top\" bgcolor=\"#ffffff\" width=\"100%\">\n                <table width=\"100%\" role=\"content-container\" class=\"outer\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">\n                  <tr>\n                    <td width=\"100%\">\n                      <table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">\n                        <tr>\n                          <td>\n                            <!--[if mso]>\n    <center>\n    <table><tr><td width=\"600\">\n  <![endif]-->\n                                    <table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"width:100%; max-width:600px;\" align=\"center\">\n                                      <tr>\n                                        <td role=\"modules-container\" style=\"padding:0px 0px 0px 0px; color:#516775; text-align:left;\" bgcolor=\"#F9F5F2\" width=\"100%\" align=\"left\"><table class=\"module preheader preheader-hide\" role=\"module\" data-type=\"preheader\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;\">\n    <tr>\n      <td role=\"module-content\">\n        <p></p>\n      </td>\n    </tr>\n  </table><table class=\"module\" role=\"module\" data-type=\"text\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"table-layout: fixed;\" data-muid=\"gNWHzBzkFeWH4JDKd2Aikk\" data-mc-module-version=\"2019-10-22\">\n      <tbody><tr>\n        <td style=\"background-color:#ffffff; padding:20px 0px 20px 0px; line-height:30px; text-align:inherit;\" height=\"100%\" valign=\"top\" bgcolor=\"#ffffff\"><div><div style=\"font-family: inherit; text-align: center\"><span style=\"font-size: 24px; color: #febc5d\"><strong></a></strong></span><span style=\"font-size: 24px\"><strong> </strong></span><span style=\"font-size: 24px; color: #00b6ac\"></span></div><div></div></div></td>\n      </tr>\n    </tbody></table><table class=\"module\" role=\"module\" data-type=\"divider\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"table-layout: fixed;\" data-muid=\"7b73dce8-5af9-490a-af42-28a48d0b8855.1\">\n    <tbody>\n      <tr>\n        <td style=\"padding:0px 0px 0px 0px;\" role=\"module-content\" height=\"100%\" valign=\"top\" bgcolor=\"\">\n          <table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" align=\"center\" width=\"100%\" height=\"1px\" style=\"line-height:1px; font-size:1px;\">\n            <tbody>\n              <tr>\n                <td style=\"padding:0px 0px 1px 0px;\" bgcolor=\"#bdbdbd\"></td>\n              </tr>\n            </tbody>\n          </table>\n        </td>\n      </tr>\n    </tbody>\n  </table><table class=\"module\" role=\"module\" data-type=\"text\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"table-layout: fixed;\" data-muid=\"bA2FfEE6abadx6yKoMr3F9\" data-mc-module-version=\"2019-10-22\">\n      <tbody><tr>\n        <td style=\"background-color:#ffffff; padding:25px 40px 25px 40px; line-height:24px; text-align:inherit;\" height=\"100%\" valign=\"top\" bgcolor=\"#ffffff\"><div><div style=\"font-family: inherit; text-align: left\"><span style=\"color: #000000\">Dear {{.User}}, <br><br>This email is to confirm that your proposal #{{.ProposalID}} was the best option and winner for the {{.EqName}}. <br><br><br> Thanks again for the opportunity! <br> </div></td>\n      </tr>\n    </tbody></table> <table class=\"module\" role=\"module\" data-type=\"divider\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"table-layout: fixed;\" data-muid=\"7b73dce8-5af9-490a-af42-28a48d0b8855\">\n    <tbody>\n      <tr>\n        <td style=\"padding:0px 0px 0px 0px;\" role=\"module-content\" height=\"100%\" valign=\"top\" bgcolor=\"\">\n          <table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" align=\"center\" width=\"100%\" height=\"1px\" style=\"line-height:1px; font-size:1px;\">\n            <tbody>\n              <tr>\n                <td style=\"padding:0px 0px 1px 0px;\" bgcolor=\"#bdbdbd\"></td>\n              </tr>\n            </tbody>\n          </table>\n        </td>\n      </tr>\n    </tbody>\n  </table><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"module\" data-role=\"module-button\" data-type=\"button\" role=\"module\" style=\"table-layout:fixed\" width=\"100%\" data-muid=\"bKHWQMgPkL5opYCkxiM6aS\"><tbody><tr><td align=\"center\" class=\"outer-td\" style=\"padding:20px 0px 0px 0px; background-color:#ffffff;\" bgcolor=\"#ffffff\"><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"button-css__deep-table___2OZyb wrapper-mobile\" style=\"text-align:center\"><tbody><tr><td align=\"center\" bgcolor=\"#febc5d\" class=\"inner-td\" style=\"border-radius:6px; font-size:16px; text-align:center; background-color:inherit;\">     </td></tr></tbody></table></td></tr></tbody></table></td>\n                                      </tr>\n                                    </table>\n                                    <!--[if mso]>\n                                  </td>\n                                </tr>\n                              </table>\n                            </center>\n                            <![endif]-->\n                          </td>\n                        </tr>\n                      </table>\n                    </td>\n                  </tr>\n                </table>\n              </td>\n            </tr>\n          </table>\n        </div>\n      </center>\n    </body>\n  </html>"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receivers
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receivers, em.as_string())