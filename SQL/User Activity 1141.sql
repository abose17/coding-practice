-- 1141. User Activity for the Past 30 Days I
-- Solved
-- Easy
-- Topics
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Activity

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | user_id       | int     |
-- | session_id    | int     |
-- | activity_date | date    |
-- | activity_type | enum    |
-- +---------------+---------+
-- This table may have duplicate rows.
-- The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
-- The table shows the user activities for a social media website. 
-- Note that each session belongs to exactly one user.
 

-- Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

-- Return the result table in any order.

-- The result format is in the following example.

# Write your MySQL query statement below
SELECT activity_date as day, COUNT(Distinct user_id) as active_users FROM Activity GROUP BY activity_date HAVING activity_date BETWEEN '2019-06-28' AND '2019-07-27';