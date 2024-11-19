# from telegram import Update
# from telegram.ext import (
#     ApplicationBuilder,
#     MessageHandler,
#     CommandHandler,
#     ContextTypes,
#     filters,
# )
# import subprocess
# import os

# # Directory for executing commands
# WORKING_DIRECTORY = "C:\\Users\\jjosh"

# # Path for the hidden folder
# HIDDEN_FOLDER = "C:\\Users\\jjosh\\.env"

# # Ensure hidden folder is created and marked as hidden
# if not os.path.exists(HIDDEN_FOLDER):
#     os.makedirs(HIDDEN_FOLDER)
#     subprocess.run(f'attrib +h "{HIDDEN_FOLDER}"', shell=True, check=True)

# # Dictionary to temporarily store user data
# user_choices = {}
# current_directory = WORKING_DIRECTORY  # Maintain the current working directory


# async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     global current_directory
#     cmd = update.message.text.strip()

#     # Only execute commands that start with "/"
#     if not cmd.startswith("/"):
#         return

#     cmd = cmd[1:].strip()

#     if not cmd:
#         await update.message.reply_text("Please provide a command to execute.")
#         return

#     # Handle `cd` command
#     if cmd.startswith("cd "):
#         target_dir = cmd[3:].strip()
#         new_directory = os.path.join(current_directory, target_dir)
#         if os.path.isdir(new_directory):
#             current_directory = new_directory
#             await update.message.reply_text(f"Directory changed to: {current_directory}")
#         else:
#             await update.message.reply_text(f"Directory not found: {new_directory}")
#         return

#     try:
#         # Execute the command in the specified directory
#         result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=current_directory)
#         output = result.stdout if result.returncode == 0 else result.stderr

#         if len(output) > 4096:
#             # Save the output in the global dictionary
#             user_choices[update.message.chat_id] = output

#             await update.message.reply_text(
#                 "The output is too long to send in a single message. "
#                 "Would you like to:\n"
#                 "1. Split the output into multiple messages\n"
#                 "2. Receive the output as a file\n\n"
#                 "Reply with `1` or `2`."
#             )
#         else:
#             await update.message.reply_text(f"```\n{output}\n```", parse_mode='Markdown')

#     except Exception as e:
#         await update.message.reply_text(f"An error occurred: {str(e)}")


# async def handle_user_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     chat_id = update.message.chat_id
#     user_choice = update.message.text.strip()

#     if chat_id not in user_choices:
#         await update.message.reply_text(
#             "You have not executed any command yet or the output is already processed."
#         )
#         return

#     output = user_choices.pop(chat_id)

#     if user_choice == "1":
#         # Split and send output in chunks
#         MAX_MESSAGE_LENGTH = 4096
#         for i in range(0, len(output), MAX_MESSAGE_LENGTH):
#             await update.message.reply_text(
#                 f"```\n{output[i:i + MAX_MESSAGE_LENGTH]}\n```",
#                 parse_mode='Markdown'
#             )
#     elif user_choice == "2":
#         # Send output as a file
#         file_path = os.path.join(HIDDEN_FOLDER, "output.txt")
#         with open(file_path, "w") as file:
#             file.write(output)
#         await update.message.reply_document(document=open(file_path, "rb"))
#     else:
#         user_choices[chat_id] = output
#         await update.message.reply_text("Invalid choice. Please reply with `1` or `2`.")


# async def send_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a help message when the /help command is used."""
    # help_text = """
    #                 For more information on a specific command, type HELP command-name
    #                 ASSOC          Displays or modifies file extension associations.
    #                 ATTRIB         Displays or changes file attributes.
    #                 BREAK          Sets or clears extended CTRL+C checking.
    #                 BCDEDIT        Sets properties in boot database to control boot loading.
    #                 CACLS          Displays or modifies access control lists (ACLs) of files.
    #                 CALL           Calls one batch program from another.
    #                 CD             Displays the name of or changes the current directory.
    #                 CHCP           Displays or sets the active code page number.
    #                 CHDIR          Displays the name of or changes the current directory.
    #                 CHKDSK         Checks a disk and displays a status report.
    #                 CHKNTFS        Displays or modifies the checking of disk at boot time.
    #                 CLS            Clears the screen.
    #                 CMD            Starts a new instance of the Windows command interpreter.
    #                 COLOR          Sets the default console foreground and background colors.
    #                 COMP           Compares the contents of two files or sets of files.
    #                 COMPACT        Displays or alters the compression of files on NTFS partitions.
    #                 CONVERT        Converts FAT volumes to NTFS.  You cannot convert the
    #                             current drive.
    #                 COPY           Copies one or more files to another location.
    #                 DATE           Displays or sets the date.
    #                 DEL            Deletes one or more files.
    #                 DIR            Displays a list of files and subdirectories in a directory.
    #                 DISKPART       Displays or configures Disk Partition properties.
    #                 DOSKEY         Edits command lines, recalls Windows commands, and
    #                             creates macros.
    #                 DRIVERQUERY    Displays current device driver status and properties.
    #                 ECHO           Displays messages, or turns command echoing on or off.
    #                 ENDLOCAL       Ends localization of environment changes in a batch file.
    #                 ERASE          Deletes one or more files.
    #                 EXIT           Quits the CMD.EXE program (command interpreter).
    #                 FC             Compares two files or sets of files, and displays the
    #                             differences between them.
    #                 FIND           Searches for a text string in a file or files.
    #                 FINDSTR        Searches for strings in files.
    #                 FOR            Runs a specified command for each file in a set of files.
    #                 FORMAT         Formats a disk for use with Windows.
    #                 FSUTIL         Displays or configures the file system properties.
    #                 FTYPE          Displays or modifies file types used in file extension
    #                             associations.
    #                 GOTO           Directs the Windows command interpreter to a labeled line in
    #                             a batch program.
    #                 GPRESULT       Displays Group Policy information for machine or user.
    #                 HELP           Provides Help information for Windows commands.
    #                 ICACLS         Display, modify, backup, or restore ACLs for files and
    #                             directories.
    #                 IF             Performs conditional processing in batch programs.
    #                 LABEL          Creates, changes, or deletes the volume label of a disk.
    #                 MD             Creates a directory.
    #                 MKDIR          Creates a directory.
    #                 MKLINK         Creates Symbolic Links and Hard Links
    #                 MODE           Configures a system device.
    #                 MORE           Displays output one screen at a time.
    #                 MOVE           Moves one or more files from one directory to another
    #                             directory.
    #                 OPENFILES      Displays files opened by remote users for a file share.
    #                 PATH           Displays or sets a search path for executable files.
    #                 PAUSE          Suspends processing of a batch file and displays a message.
    #                 POPD           Restores the previous value of the current directory saved by
    #                             PUSHD.
    #                 PRINT          Prints a text file.
    #                 PROMPT         Changes the Windows command prompt.
    #                 PUSHD          Saves the current directory then changes it.
    #                 RD             Removes a directory.
    #                 RECOVER        Recovers readable information from a bad or defective disk.
    #                 REM            Records comments (remarks) in batch files or CONFIG.SYS.
    #                 REN            Renames a file or files.
    #                 RENAME         Renames a file or files.
    #                 REPLACE        Replaces files.
    #                 RMDIR          Removes a directory.
    #                 ROBOCOPY       Advanced utility to copy files and directory trees
    #                 SET            Displays, sets, or removes Windows environment variables.
    #                 SETLOCAL       Begins localization of environment changes in a batch file.
    #                 SC             Displays or configures services (background processes).
    #                 SCHTASKS       Schedules commands and programs to run on a computer.
    #                 SHIFT          Shifts the position of replaceable parameters in batch files.
    #                 SHUTDOWN       Allows proper local or remote shutdown of machine.
    #                 SORT           Sorts input.
    #                 START          Starts a separate window to run a specified program or command.
    #                 SUBST          Associates a path with a drive letter.
    #                 SYSTEMINFO     Displays machine specific properties and configuration.
    #                 TASKLIST       Displays all currently running tasks including services.
    #                 TASKKILL       Kill or stop a running process or application.
    #                 TIME           Displays or sets the system time.
    #                 TITLE          Sets the window title for a CMD.EXE session.
    #                 TREE           Graphically displays the directory structure of a drive or
    #                             path.
    #                 TYPE           Displays the contents of a text file.
    #                 VER            Displays the Windows version.
    #                 VERIFY         Tells Windows whether to verify that your files are written
    #                             correctly to a disk.
    #                 VOL            Displays a disk volume label and serial number.
    #                 XCOPY          Copies files and directory trees.
    #                 WMIC           Displays WMI information inside interactive command shell.

    #                 For more information on tools see the command-line reference in the online help.
    #                 """

#     await update.message.reply_text(help_text)


# # Telegram bot setup
# app = ApplicationBuilder().token("7855402197:AAHpqf0g_wfSErbBt9aJl3vAk2awEUhKyYY").build()

# # Add message handlers
# app.add_handler(CommandHandler("help", send_help))  # Add the /help command handler
# app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^/.*'), execute_command))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_choice))

# if __name__ == "__main__":
#     app.run_polling()


from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)
import os
import sys
import subprocess

# Directory for executing commands
WORKING_DIRECTORY = "C:\\Users\\jjosh"
HIDDEN_FOLDER = "C:\\Users\\jjosh\\.env"

# Ensure hidden folder is created and marked as hidden
if not os.path.exists(HIDDEN_FOLDER):
    os.makedirs(HIDDEN_FOLDER)
    subprocess.run(f'attrib +h "{HIDDEN_FOLDER}"', shell=True, check=True)

# Dictionary to temporarily store user data
user_choices = {}
current_directory = WORKING_DIRECTORY  # Maintain the current working directory


async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_directory
    cmd = update.message.text.strip()

    if not cmd.startswith("/"):
        return

    cmd = cmd[1:].strip()

    if not cmd:
        await update.message.reply_text("Please provide a command to execute.")
        return

    # Handle `cd` command
    if cmd.startswith("cd "):
        target_dir = cmd[3:].strip()
        new_directory = os.path.join(current_directory, target_dir)
        if os.path.isdir(new_directory):
            current_directory = new_directory
            await update.message.reply_text(f"Directory changed to: {current_directory}")
        else:
            await update.message.reply_text(f"Directory not found: {new_directory}")
        return

    try:
        # Execute the command in the specified directory
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=current_directory)
        output = result.stdout if result.returncode == 0 else result.stderr

        if len(output) > 4096:
            # Save the output in the global dictionary
            user_choices[update.message.chat_id] = output

            await update.message.reply_text(
                "The output is too long to send in a single message. "
                "Would you like to:\n"
                "1. Split the output into multiple messages\n"
                "2. Receive the output as a file\n\n"
                "Reply with `1` or `2`."
            )
        else:
            await update.message.reply_text(f"```\n{output}\n```", parse_mode='Markdown')

    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


async def handle_user_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    user_choice = update.message.text.strip()

    if chat_id not in user_choices:
        await update.message.reply_text(
            "You have not executed any command yet or the output is already processed."
        )
        return

    output = user_choices.pop(chat_id)

    if user_choice == "1":
        MAX_MESSAGE_LENGTH = 4096
        for i in range(0, len(output), MAX_MESSAGE_LENGTH):
            await update.message.reply_text(
                f"```\n{output[i:i + MAX_MESSAGE_LENGTH]}\n```",
                parse_mode='Markdown'
            )
    elif user_choice == "2":
        file_path = os.path.join(HIDDEN_FOLDER, "output.txt")
        with open(file_path, "w") as file:
            file.write(output)
        await update.message.reply_document(document=open(file_path, "rb"))
    else:
        user_choices[chat_id] = output
        await update.message.reply_text("Invalid choice. Please reply with `1` or `2`.")


async def send_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
    
                    For more information on a specific command, type HELP command-name
                    ASSOC          Displays or modifies file extension associations.
                    ATTRIB         Displays or changes file attributes.
                    BREAK          Sets or clears extended CTRL+C checking.
                    BCDEDIT        Sets properties in boot database to control boot loading.
                    CACLS          Displays or modifies access control lists (ACLs) of files.
                    CALL           Calls one batch program from another.
                    CD             Displays the name of or changes the current directory.
                    CHCP           Displays or sets the active code page number.
                    CHDIR          Displays the name of or changes the current directory.
                    CHKDSK         Checks a disk and displays a status report.
                    CHKNTFS        Displays or modifies the checking of disk at boot time.
                    CLS            Clears the screen.
                    CMD            Starts a new instance of the Windows command interpreter.
                    COLOR          Sets the default console foreground and background colors.
                    COMP           Compares the contents of two files or sets of files.
                    COMPACT        Displays or alters the compression of files on NTFS partitions.
                    CONVERT        Converts FAT volumes to NTFS.  You cannot convert the
                                current drive.
                    COPY           Copies one or more files to another location.
                    DATE           Displays or sets the date.
                    DEL            Deletes one or more files.
                    DIR            Displays a list of files and subdirectories in a directory.
                    DISKPART       Displays or configures Disk Partition properties.
                    DOSKEY         Edits command lines, recalls Windows commands, and
                                creates macros.
                    DRIVERQUERY    Displays current device driver status and properties.
                    ECHO           Displays messages, or turns command echoing on or off.
                    ENDLOCAL       Ends localization of environment changes in a batch file.
                    ERASE          Deletes one or more files.
                    EXIT           Quits the CMD.EXE program (command interpreter).
                    FC             Compares two files or sets of files, and displays the
                                differences between them.
                    FIND           Searches for a text string in a file or files.
                    FINDSTR        Searches for strings in files.
                    FOR            Runs a specified command for each file in a set of files.
                    FORMAT         Formats a disk for use with Windows.
                    FSUTIL         Displays or configures the file system properties.
                    FTYPE          Displays or modifies file types used in file extension
                                associations.
                    GOTO           Directs the Windows command interpreter to a labeled line in
                                a batch program.
                    GPRESULT       Displays Group Policy information for machine or user.
                    HELP           Provides Help information for Windows commands.
                    ICACLS         Display, modify, backup, or restore ACLs for files and
                                directories.
                    IF             Performs conditional processing in batch programs.
                    LABEL          Creates, changes, or deletes the volume label of a disk.
                    MD             Creates a directory.
                    MKDIR          Creates a directory.
                    MKLINK         Creates Symbolic Links and Hard Links
                    MODE           Configures a system device.
                    MORE           Displays output one screen at a time.
                    MOVE           Moves one or more files from one directory to another
                                directory.
                    OPENFILES      Displays files opened by remote users for a file share.
                    PATH           Displays or sets a search path for executable files.
                    PAUSE          Suspends processing of a batch file and displays a message.
                    POPD           Restores the previous value of the current directory saved by
                                PUSHD.
                    PRINT          Prints a text file.
                    PROMPT         Changes the Windows command prompt.
                    PUSHD          Saves the current directory then changes it.
                    RD             Removes a directory.
                    RECOVER        Recovers readable information from a bad or defective disk.
                    REM            Records comments (remarks) in batch files or CONFIG.SYS.
                    REN            Renames a file or files.
                    RENAME         Renames a file or files.
                    REPLACE        Replaces files.
                    RMDIR          Removes a directory.
                    ROBOCOPY       Advanced utility to copy files and directory trees
                    SET            Displays, sets, or removes Windows environment variables.
                    SETLOCAL       Begins localization of environment changes in a batch file.
                    SC             Displays or configures services (background processes).
                    SCHTASKS       Schedules commands and programs to run on a computer.
                    SHIFT          Shifts the position of replaceable parameters in batch files.
                    SHUTDOWN       Allows proper local or remote shutdown of machine.
                    SORT           Sorts input.
                    START          Starts a separate window to run a specified program or command.
                    SUBST          Associates a path with a drive letter.
                    SYSTEMINFO     Displays machine specific properties and configuration.
                    TASKLIST       Displays all currently running tasks including services.
                    TASKKILL       Kill or stop a running process or application.
                    TIME           Displays or sets the system time.
                    TITLE          Sets the window title for a CMD.EXE session.
                    TREE           Graphically displays the directory structure of a drive or
                                path.
                    TYPE           Displays the contents of a text file.
                    VER            Displays the Windows version.
                    VERIFY         Tells Windows whether to verify that your files are written
                                correctly to a disk.
                    VOL            Displays a disk volume label and serial number.
                    XCOPY          Copies files and directory trees.
                    WMIC           Displays WMI information inside interactive command shell.

                    For more information on tools see the command-line reference in the online help.
                    

    """
    await update.message.reply_text(help_text)


async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_directory
    current_directory = HIDDEN_FOLDER  # Reset directory on restart
    await update.message.reply_text("Restarting the bot... Please wait.")
    os.execl(sys.executable, sys.executable, *sys.argv)


async def upload_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.document:
        file = await update.message.document.get_file()
        file_path = os.path.join(HIDDEN_FOLDER, update.message.document.file_name)
        await file.download(file_path)
        await update.message.reply_text(f"File uploaded to: {file_path}")


async def delete_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_name = update.message.text.strip().split(" ", 1)[1]
    file_path = os.path.join(current_directory, file_name)
    try:
        os.remove(file_path)
        await update.message.reply_text(f"File deleted: {file_path}")
    except FileNotFoundError:
        await update.message.reply_text("File not found.")
    except Exception as e:
        await update.message.reply_text(f"Error deleting file: {str(e)}")


async def rename_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = update.message.text.strip().split(" ", 2)
    if len(args) != 3:
        await update.message.reply_text("Usage: /rename <old_name> <new_name>")
        return
    old_name, new_name = args[1], args[2]
    old_path = os.path.join(current_directory, old_name)
    new_path = os.path.join(current_directory, new_name)
    try:
        os.rename(old_path, new_path)
        await update.message.reply_text(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        await update.message.reply_text("File not found.")
    except Exception as e:
        await update.message.reply_text(f"Error renaming file: {str(e)}")


# Telegram bot setup
app = ApplicationBuilder().token("7855402197:AAHpqf0g_wfSErbBt9aJl3vAk2awEUhKyYY").build()

# Add message handlers
app.add_handler(CommandHandler("help", send_help))
app.add_handler(CommandHandler("restart", restart))
app.add_handler(MessageHandler(filters.Document.ALL, upload_file))
app.add_handler(MessageHandler(filters.Regex("^/delete "), delete_file))
app.add_handler(MessageHandler(filters.Regex("^/rename "), rename_file))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^/.*'), execute_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_choice))

if __name__ == "__main__":
    app.run_polling()



