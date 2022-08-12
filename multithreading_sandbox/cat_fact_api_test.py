import CAT_FACT_API

# driver code
if __name__ == "__main__":
    given_length = 88
    try:
        response_json = CAT_FACT_API.get_cat_fact_by_length(max_length=given_length)
        print(f"response.json(): {response_json}")
    except Exception as e:
        print(f"Exception occured: {e}")
