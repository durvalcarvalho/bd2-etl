from fsplit.filesplit import Filesplit

fs = Filesplit()

fs.split(file='main.csv', split_size=800000000, output_dir='files', include_header=True)
