:: Adds all changes, commits them with the given message, and pushes them to main
@ECHO OFF
SETLOCAL enabledelayedexpansion
SET TASK_NAME=Publish to GitHub
SET LOG_PREFIX=[publish]
SET COMMIT_MESSAGE=%1
SET RED=[31m
SET GREEN=[32m
SET RESET=[0m

git add .
GOTO :GET_COMMIT_MESSAGE

:GET_COMMIT_MESSAGE
IF "%COMMIT_MESSAGE%" NEQ "" GOTO :PUBLISH
ECHO %RED%Commit message cannot be empty%RESET%
SET /P COMMIT_MESSAGE=Enter commit message: 
GOTO :GET_COMMIT_MESSAGE

:PUBLISH
git commit --message="[publish] !COMMIT_MESSAGE!"
git push -u origin main
IF %ERRORLEVEL% NEQ 0 (
    ECHO %LOG_PREFIX% %RED%%TASK_NAME% failed with error code %ERRORLEVEL%%RESET%
) ELSE (
    SET URL=https://github.com/aeckar/usf-cse-resources
    ECHO %LOG_PREFIX% %GREEN%%TASK_NAME% succeeded:%RESET% !URL!
)