## MYSQL : learner_choi database

queries = {
    "item_his" : "SELECT * FROM item_his WHERE proc_ymd = '{batch_date}'",
    "point_his" :   "SELECT * FROM point_his WHERE proc_ymd = '{batch_date}'",
    "regdate_his" : "SELECT * FROM regdate_his WHERE regdate = '{batch_date}'",
    "study_his" :   "SELECT * FROM study_his WHERE proc_ymd = '{batch_date}'",
    "member" :   "SELECT * FROM member"
}