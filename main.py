import argparse
def train(document_path, y):
    print("training")

# Should Return yes/no
def classify(document_path):
    print("classification")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run with -h flag for help', prog='Document Classifier')
    parser.add_argument('option',  default=True, type= bool, choices=[True, False])
    parser.add_argument('y', choices=[0, 1], type=int)
    parser.add_argument('-p', default='./', type=str,dest='path')
    args = parser.parse_args()

    if(args.option):
        train(args.path, args.y)
    else:
        classify(args.path)



