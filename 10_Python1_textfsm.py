import textfsm
from io import StringIO

def parse_traceroute_output(traceroute_output):
    # Define the template for parsing traceroute output
    template = """
    Value Hop (\d+)
    Value IP (\S+)
    Value Host (\S+)
    Value Loss (\d+)
    Value Snt (\d+)
    Value Last (\d+\.\d+|\d+)
    Value Avg (\d+\.\d+|\d+)
    Value Best (\d+\.\d+|\d+)
    Value Wrst (\d+\.\d+|\d+)
    Value StDev (\d+\.\d+|\d+)

    Start
      ^${Hop}\s+${IP}\s+${Host}\s+${Loss}\s+${Snt}\s+${Last}\s+${Avg}\s+${Best}\s+${Wrst}\s+${StDev} -> Record
    """
    
    # Create a TextFSM object
    fsm = textfsm.TextFSM(StringIO(template))
    
    # Parse the traceroute output
    parsed_results = fsm.ParseText(traceroute_output)
    
    return parsed_results

if __name__ == "__main__":
    # Example traceroute output
    traceroute_output = """
    1  192.168.1.1 (192.168.1.1)  1.128 ms  1.128 ms  1.165 ms
    2  10.10.1.1 (10.10.1.1)  2.057 ms  2.056 ms  2.062 ms
    3  203.0.113.1 (203.0.113.1)  3.050 ms  3.048 ms  3.051 ms
    """
    
    # Parse the traceroute output
    parsed_results = parse_traceroute_output(traceroute_output)
    
    # Display the parsed results
    print(parsed_results)