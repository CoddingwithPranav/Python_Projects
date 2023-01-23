import os 
def  isBond( filename):
    with open(filename ,"r") as f:
        filecontent  = f.read()
    if "binod" in filecontent.lower():
        return True
    else:
        return False
    
if __name__ == "__main__":
    dir_contents = os.listdir()
    nBinod = 0
    print(dir_contents)
    for item in dir_contents:
        if item.endswith('.txt'):
            print(f"Detecting Binod in {item}")
            flag = isBond(item)
            if flag :
                print(f"Binod found in {item} ")
                nBinod = nBinod + 1
                
    print("**********Binod Detector Summary")
    print(f"{nBinod} file found with binnod into them")