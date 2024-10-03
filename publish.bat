@echo off
SETLOCAL enabledelayedexpansion
SET TASK_NAME=Publish to GitHub

git add .
git commit --message="[publish] Add information"
git push --upstream origin main

IF %ERRORLEVEL% NEQ 0 (
    ECHO %TASK_NAME% failed with error code %ERRORLEVEL%
) ELSE (
    FOR /F "tokens=* USEBACKQ" %%F IN (`git config --get remote.origin.url`) DO (
        SET URL=%%F
    )
    ECHO %TASK_NAME% succeeded: !URL!
)