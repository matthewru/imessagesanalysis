# imessagesanalysis


SQL Script:

SELECT ROWID, text, is_from_me, handle_id, 
   date AS date_utc
FROM message T1 
INNER JOIN chat_message_join T2 
    ON T2.chat_id = 81
    AND T1.ROWID = T2.message_id 
ORDER BY T1.date;