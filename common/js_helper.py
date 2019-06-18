def scroll_into_element(driver, el):
    driver.execute_script("arguments[0].scrollIntoView();", el)