@ECHO OFF
SETLOCAL enabledelayedexpansion
SET TASK_NAME=Publish to GitHub
SET LOG_PREFIX=[publish]
SET COMMIT_MESSAGE=%1
SET RED=[31m
SET GREEN=[32m
SET RESET=[0m

GOTO :PUBLISH

:: Adds all recent changes to git, commits them with an optional message, then pushes them to the main
:PUBLISH
git add .
IF "%COMMIT_MESSAGE%"=="" (
    git commit
) ELSE (
    git commit --message="[publish] %COMMIT_MESSAGE%"
)
git push -u origin main
GOTO :LOG_ERROR

:: Prints whether the operation was successful or not
:LOG_ERROR
IF %ERRORLEVEL% NEQ 0 (
    ECHO %LOG_PREFIX% %RED%%TASK_NAME% failed with error code %ERRORLEVEL%%RESET%
) ELSE (
    SET URL=https://github.com/aeckar/usf-cse-resources
    ECHO %LOG_PREFIX% %GREEN%%TASK_NAME% succeeded:%RESET% !URL!
)