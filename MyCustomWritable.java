


import org.apache.hadoop.util.StringUtils;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.io.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.io.compress.*;
import org.apache.hadoop.mapreduce.lib.output.*;

import java.net.URI;
import java.net.URISyntaxException;



import java.io.IOException;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.DataOutputStream;
import java.io.DataInputStream;
import java.io.OutputStream;
import java.io.InputStream;
import java.io.EOFException;
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.util.Calendar;
import java.util.Date;
import java.sql.Timestamp;


import org.apache.hadoop.io.Writable;

//import com.emc.greenplum.gpdb.hadoop.io.GPDBWritable;



public class MyCustomWritable implements Writable
{
	public int int1;
	public byte circle;
			
	public MyCustomWritable()
	{
	
		// 1. num1	
		int1 = 0;
		// 2. circle
		circle = '\n';
	}
	
	public MyCustomWritable(int i1, int i2, int i3)
	{
	
		// 1. num
		int1   = i1;
                circle = (byte)i2;	
	}
	
	int GetInt1()
	{
		return int1;
	}
	
	byte GetCircle()
	{
		return circle;
	}

	public void write(DataOutput out) throws IOException 
	{
		
		// 1. int1
		IntWritable intw = new IntWritable();
		
		intw.set(int1);
		intw.write(out);
		
	 	// 2. circle
		intw.set(circle);
		intw.write(out);
	}
	
	public void readFields(DataInput in) throws IOException
	{
				
		// 1. int1
		IntWritable intw = new IntWritable();
		
		intw.readFields(in);
		int1 = intw.get();
	
		// 2. circle
		intw.readFields(in);
		circle = (byte)intw.get();
	}
	
	public void printFieldTypes()
	{
		Class myClass = this.getClass();
		Field[] fields = myClass.getDeclaredFields();

		for (int i = 0; i < fields.length; i++) 
		{
			System.out.println(fields[i].getType().getName());
		}
	}
}	
	
























