# https://leetcode.com/problems/course-schedule/

class Solution(object):


   

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # convert the prerequisites to a different structure, where the index is the course id and the list inside the prereqs.
        prereqs = []
        for idx in range(0, numCourses):
            prereqs.append([])
        
        # first scan - o(n)
        for input in prerequisites:
            #print(input)
            course = input[0]
            preq = input[1]
            # there can be more than one dependency for each course
            prereqs[course].append(preq)
            #print(prereqs)

            
        #print(prereqs)
        visited = [False] * numCourses
        
        def calc_reqs(course):
            """ A recursive function that traverses the graph and checks if there are loop.
            If a loop is encoutered, return immediately with True.
            After each iteration on the prereqisites of a course, update the prereqs list of the course
            with all of the new prereqs gathered from its neighbours. That way if a course is "visited"
            we know that we already have the full list of all of its dependencies so no further traversing is required.
            
            :type course: int
            :rtype: bool
            """
            
            #print(course)
            course_prereqs = prereqs[course]
            # if the course was visited, we assume that its reqs are already fully calculated. So it's enough to check if there is a loop 
            # with the reqs.
            if visited[course]:
                return course in set(course_prereqs)
            
            visited[course] = True
            new_reqs = set()
            
            for req in course_prereqs:
                #print("req: %d" % req)
                if not visited[req]:
                    if calc_reqs(req):
                        # there is a loop, return immediately
                        return True
                req_reqs = set(prereqs[req])
                if course in req_reqs:
                    return True
                new_reqs = new_reqs.union(req_reqs - set(course_prereqs))
                
            # add the new reqs to the list of the course's reqs for next iterations.
            # note: we don't add the new reqs in the middle of the iteration, because all of the 
            # reqs added in new_reqs are already fully calculated, so there is no need to traverse them again.
            prereqs[course].extend(list(new_reqs))
            # if we got to this stage, there is no loop for this course.
            return False
            
        loop = False
        # go through all courses, and check if each one doesn't have itself in the prereqs. 
        # If all pass, there is no loop in the graph of dependencies and the courses can be finished.
        for course in range(0, numCourses):
            if calc_reqs(course):
                loop = True
                break
                
        return not loop
        
