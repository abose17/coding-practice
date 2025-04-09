-- 180. Consecutive Numbers
-- Solved
-- Medium
-- Topics
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column starting from 1.
 

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.


# Write your MySQL query statement below
SELECT DISTINCT L1.num as ConsecutiveNums FROM Logs L1, Logs L2, Logs L3 WHERE L1.Id = L2.Id-1 AND L2.Id = L3.Id-1 AND L1.num = L2.num AND L2.num = L3.num;