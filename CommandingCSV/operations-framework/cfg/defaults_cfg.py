FAKE_PASS_ID = "d8d7a45b-3cba-4e62-84e9-ae7f02bfd7e5"
SUFFIX = ""
SAT_ID = "padre-flatsat"

# Throw an error if the user has not set the FAKE_PASS_ID, SAT_ID
if FAKE_PASS_ID == "" or SAT_ID == "":
    raise Exception("Please set the FAKE_PASS_ID, SAT_ID in the cfg/defaults_cfg.py file.")
