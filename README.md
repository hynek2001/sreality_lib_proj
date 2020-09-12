#### sreality api  

test library for sreality.cz ..

###### instalace  
    ```
    pip install git+git://github.com/hynek2001/sreality_lib_proj.git
    ```
     

##### hlavni funkce
* dotaz na sreality  
    ```python  
    from srealitylib.coldb import querySreality
    sfilter={
        "category_main_cb": 1,
        #"category_sub_cb":"11|12",
        "category_type_cb": 1,
        #"locality_region_id": 10,
    }
    querySreality(sfilter)
    ```
    


##### pomocne funkce

* overeni parametru:  
    ```python
    from srealitylib.coldb import srealityStableParams
    srealityStableParams()
    ```
    vylistuje % vyskytu jednotlivych parametru..  
    
* overeni zda hash_id je unikatni   
    ```python
    from srealitylib.coldb import ishashidUnique
    ishashidUnique()  
    ```

    
    
    
    
    